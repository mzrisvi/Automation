# This is for collections-related utilities.
sub = ['python', 'java', 'cpp', 'javascript', 'ruby', 'go', 'rust']
print(sub[0])
sub[2] = 'typescript'
print('1:',sub)

sub = {'python', 'java', 'java', 'javascript', 'ruby', 'go', 'rust'}
print('2:',sub)

sub = ('python', 'java', 'cpp', 'javascript', 'ruby', 'go', 'rust')
#sub[3] = 'typescript'  # This will raise an error
print('3:',sub)

dict_sub = {'one': 'python', 'two': 'java', 'three': 'cpp', 'four': 'javascript'}
print('4:',dict_sub)
dict_sub['five'] = 'ruby'
print('5:',dict_sub)

