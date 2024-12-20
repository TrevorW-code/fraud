def test_from_template_module_level_basic():
    import fraud as fr
    out = fr.from_template("Hi! Please meet my friend {name}.",10)
    print(out)

def test_from_template_module_level_custom():
    import fraud as fr
    
    def special_company(x):
        if x == "special_company":
            return "RANDOM_CUSTOM_COMPANY"
        return None

    out = fr.from_template("{name} works at {special_company}", 10, extra_methods=[special_company])
    print(out)