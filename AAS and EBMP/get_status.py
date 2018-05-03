import cognitive_face as CF
from global_variables import personGroupId

Key = '43ed47ef01b24d79b9428bd8fe347c14'
CF.Key.set(Key)

res = CF.person_group.get_status(personGroupId)
print res
