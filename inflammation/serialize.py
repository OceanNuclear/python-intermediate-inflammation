import json

# A pertinent question: why care about using json?

class PatientSerializer:
    @classmethod
    def serialize(cls, instances):
        return [{
            'name': inst.name,
            'observations': inst.observations
        } for inst in instances]

    @classmethod
    def deserialize(cls, data):
        from inflammation.models import Patient, Observation
        read_data = []
        for dic in data:
            read_data.append(Patient(dic['name']))
            if dic.get('observations', []):
                read_data[-1].observations = [Observation(**d) for d in dic['observatins']]
        return read_data

class PatientJSONSerializer(PatientSerializer):
    @classmethod
    def save(cls, instances, path):
        with open(path, 'w') as jf:
            # json.dump can only handle dictionaries.
            # print(path)
            json.dump(cls.serialize(instances), jf)

    @classmethod
    def load(cls, path):
        with open(path) as jf:
            data = json.load(jf)
        return cls.deserialize(data)