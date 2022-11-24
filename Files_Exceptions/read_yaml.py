import yaml

filepath1 = "../Data/credentials.yml"

with open(filepath1, "r") as stream:
    credentials = yaml.safe_load(stream)

uname = credentials["qa"]["username"]
print(uname)
qa_u = credentials["qa"]["username"]
qa_p = credentials["uat"]["password"]
print(f"Username: {qa_u} and password: {qa_p}")

