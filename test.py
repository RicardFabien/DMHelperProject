from CharacterPortfolio import CharacterPortfolio

c = CharacterPortfolio()
c.add_character("test")

print(c.add_attribute("test", "test", "2"))

print(c.find_by_name("test").stats)


