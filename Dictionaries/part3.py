#Add list into dictionary
travel_log={
    "France":{"cities":["Lille","Paris","Dijon"],"total_visits":12,"venues_found":14},
    "Germany":{"cities":["Berlin","Hamburg", "Stuttgart"],"total_visits":32,"venues_found":10},
}

#Nesting a dictionary in a list
travel_log=[
    {
    "Country":"France",
    "cities":["Lille","Paris","Dijon"],
    "total_visits":12,
    "venues_found":14
    },
    {
      "Country":"Germany",
      "cities":["Berlin","Hamburg", "Stuttgart"],
      "total_visits":32,
      "venues_found":10
    },

]

print(travel_log)