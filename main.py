from db.comrades import datawiz_team


def pretty_print(data: list):
    for index, element in enumerate(data):
        print(f"{index+1}) {element}")



def main():
    print("My team:")
    pretty_print(datawiz_team)

if __name__=="__main__":
    main()
