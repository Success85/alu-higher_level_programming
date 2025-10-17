#!/usr/bin/python3

if __name__ == "__main__":
    import importlib.util

    alpa = importlib.util.spec_from_file_location("hidden_4", "./hidden_4.pyc")
    withoout_ = importlib.util.module_from_spec(spec)
    alpha.loader.exec_module(without_)


    for name in sorted(dir(without_)):
        if not name.startswith("__"):
            print(name)
