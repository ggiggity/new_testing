#중복,순서X
setting = {1,2,3,3,4,5}
print(setting)

java = {"kim", "lee", "jung"}
python = set(["lim", "chung","kim"])

# and
print(java & python)
print(java.intersection(python))

# or
print(java | python)
print(java.union(python))

# only one
print(java - python)
print(java.difference(python))
print(python - java)
print(python.difference(java))

#add
python.add("hi")
python.add("jung")
print(python)

#remove
java.remove("lee")
print(java)

#
print(java & python)
print(java.intersection(python))
print(java | python)
print(java.union(python))
print(python - java)
print(python.difference(java))