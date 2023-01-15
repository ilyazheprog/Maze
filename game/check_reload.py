from os import system


if __name__ == "__main__":
    from json import loads, dumps

    with open("src/config.json") as f:
        global_settings = loads(f.read())
        print(global_settings)
        if global_settings["reload"]:
            global_settings["reload"] = False
            with open("src/config.json", "w") as f:
                f.write(dumps(global_settings, indent=4))
            system("run.bat")