fake_manufacturer_db = [
    {"id": 1, "name": "Volkswagen", "nationality": "German"},
    {"id": 2, "name": "Ford", "nationality": "American"},
    {"id": 3, "name": "Honda", "nationality": "Japanese"},
    {"id": 4, "name": "Toyota", "nationality": "Japanese"},
    {"id": 5, "name": "Mazda", "nationality": "Japanese"},
    {"id": 6, "name": "Hyundai", "nationality": "South Korean"},
    {"id": 7, "name": "Kia", "nationality": "South Korean"},
    {"id": 8, "name": "Peugeot", "nationality": "French"},
    {"id": 9, "name": "Renault", "nationality": "French"},
    {"id": 10, "name": "Mini", "nationality": "British"},
    {"id": 11, "name": "Audi", "nationality": "German"},
    {"id": 12, "name": "BMW", "nationality": "German"},
    {"id": 13, "name": "Mercedes-Benz", "nationality": "German"},
    {"id": 14, "name": "Volvo", "nationality": "Swedish"},
    {"id": 15, "name": "Seat", "nationality": "Spanish"},
    {"id": 16, "name": "Skoda", "nationality": "Czech"},
    {"id": 17, "name": "Suzuki", "nationality": "Japanese"},
    {"id": 18, "name": "Nissan", "nationality": "Japanese"},
    {"id": 19, "name": "Chevrolet", "nationality": "American"},
    {"id": 20, "name": "Mitsubishi", "nationality": "Japanese"},
    {"id": 21, "name": "Fiat", "nationality": "Italian"},
    {"id": 22, "name": "Opel", "nationality": "German"},
    {"id": 23, "name": "Citroën", "nationality": "French"},
    {"id": 24, "name": "Subaru", "nationality": "Japanese"},
    {"id": 25, "name": "Alfa Romeo", "nationality": "Italian"},
    {"id": 26, "name": "DS Automobiles", "nationality": "French"},
]


fake_car_db = [
    {
        "name": "Volkswagen Golf",
        "description": "The Volkswagen Golf is a compact car known for its build quality and smooth ride.",
        "year": 2020,
        "manufacturer_id": 1,
        "categories": ["Hatchback", "Compact"],
        "features": [
            "Automatic Climate Control",
            "Bluetooth Connectivity",
            "Rearview Camera",
        ],
    },
    {
        "name": "Ford Fiesta",
        "description": "The Ford Fiesta is a fun-to-drive subcompact car with a stylish design.",
        "year": 2019,
        "manufacturer_id": 2,
        "categories": ["Hatchback", "Subcompact"],
        "features": ["Voice Control", "Cruise Control", "Heated Seats"],
    },
    {
        "name": "Honda Civic",
        "description": "The Honda Civic offers a blend of sporty performance and practicality.",
        "year": 2021,
        "manufacturer_id": 3,
        "categories": ["Hatchback", "Compact"],
        "features": ["Apple CarPlay", "Android Auto", "Adaptive Cruise Control"],
    },
    {
        "name": "Toyota Corolla",
        "description": "The Toyota Corolla is a reliable hatchback with excellent fuel efficiency.",
        "year": 2022,
        "manufacturer_id": 4,
        "categories": ["Hatchback", "Compact"],
        "features": [
            "Lane Departure Warning",
            "Automatic High Beams",
            "Blind Spot Monitor",
        ],
    },
    {
        "name": "Mazda3",
        "description": "The Mazda3 is a stylish hatchback with a premium interior and engaging driving dynamics.",
        "year": 2021,
        "manufacturer_id": 5,
        "categories": ["Hatchback", "Compact"],
        "features": ["Heads-Up Display", "Leather Seats", "Bose Sound System"],
    },
    {
        "name": "Hyundai i30",
        "description": "The Hyundai i30 is a versatile hatchback with a comfortable ride and advanced safety features.",
        "year": 2020,
        "manufacturer_id": 6,
        "categories": ["Hatchback", "Compact"],
        "features": ["Wireless Charging", "Sunroof", "Rear Parking Sensors"],
    },
    {
        "name": "Kia Ceed",
        "description": "The Kia Ceed is a practical hatchback with a spacious interior and good fuel economy.",
        "year": 2019,
        "manufacturer_id": 7,
        "categories": ["Hatchback", "Compact"],
        "features": ["Navigation System", "DAB Radio", "Reversing Camera"],
    },
    {
        "name": "Peugeot 308",
        "description": "The Peugeot 308 is a stylish hatchback with a refined interior and efficient engines.",
        "year": 2022,
        "manufacturer_id": 8,
        "categories": ["Hatchback", "Compact"],
        "features": ["Panoramic Roof", "Massage Seats", "Adaptive Headlights"],
    },
    {
        "name": "Renault Clio",
        "description": "The Renault Clio is a chic and agile hatchback with a comfortable interior.",
        "year": 2021,
        "manufacturer_id": 9,
        "categories": ["Hatchback", "Subcompact"],
        "features": ["Keyless Entry", "Ambient Lighting", "Traffic Sign Recognition"],
    },
    {
        "name": "Mini Cooper",
        "description": "The Mini Cooper is a fun-to-drive hatchback with a distinctive design.",
        "year": 2020,
        "manufacturer_id": 10,
        "categories": ["Hatchback", "Subcompact"],
        "features": ["LED Headlights", "Sport Mode", "Harman Kardon Sound System"],
    },
    {
        "name": "Audi A3",
        "description": "The Audi A3 is a premium hatchback with a luxurious interior and advanced technology.",
        "year": 2021,
        "manufacturer_id": 11,
        "categories": ["Hatchback", "Compact"],
        "features": [
            "Virtual Cockpit",
            "Wireless Apple CarPlay",
            "Bang & Olufsen Sound System",
        ],
    },
    {
        "name": "BMW 1 Series",
        "description": "The BMW 1 Series is a sporty hatchback with dynamic handling and a high-quality interior.",
        "year": 2022,
        "manufacturer_id": 12,
        "categories": ["Hatchback", "Compact"],
        "features": ["Gesture Control", "Automatic Parking", "M Sport Suspension"],
    },
    {
        "name": "Mercedes-Benz A-Class",
        "description": "The Mercedes-Benz A-Class is a sophisticated hatchback with cutting-edge technology.",
        "year": 2021,
        "manufacturer_id": 13,
        "categories": ["Hatchback", "Compact"],
        "features": [
            "MBUX Infotainment",
            "Augmented Reality Navigation",
            "Burmester Surround Sound",
        ],
    },
    {
        "name": "Volvo V40",
        "description": "The Volvo V40 is a safe and stylish hatchback with a premium interior.",
        "year": 2020,
        "manufacturer_id": 14,
        "categories": ["Hatchback", "Compact"],
        "features": [
            "City Safety System",
            "Heated Windscreen",
            "Digital Instrument Cluster",
        ],
    },
    {
        "name": "Seat Leon",
        "description": "The Seat Leon is a sporty hatchback with a modern design and advanced technology.",
        "year": 2021,
        "manufacturer_id": 15,
        "categories": ["Hatchback", "Compact"],
        "features": [
            "Full LED Headlights",
            "Wireless Charger",
            "Dynamic Chassis Control",
        ],
    },
    {
        "name": "Skoda Scala",
        "description": "The Skoda Scala is a practical hatchback with a spacious interior and smart features.",
        "year": 2022,
        "manufacturer_id": 16,
        "categories": ["Hatchback", "Compact"],
        "features": ["Virtual Cockpit", "Heated Steering Wheel", "SmartLink+"],
    },
    {
        "name": "Suzuki Swift",
        "description": "The Suzuki Swift is a nimble and efficient hatchback with a distinctive look.",
        "year": 2020,
        "manufacturer_id": 17,
        "categories": ["Hatchback", "Subcompact"],
        "features": ["Rear Cross Traffic Alert", "LED Rear Lights", "Sport Seats"],
    },
    {
        "name": "Nissan Leaf",
        "description": "The Nissan Leaf is an electric hatchback with impressive range and advanced technology.",
        "year": 2021,
        "manufacturer_id": 18,
        "categories": ["Hatchback", "Electric"],
        "features": ["ProPILOT Assist", "e-Pedal", "Around View Monitor"],
    },
    {
        "name": "Chevrolet Bolt",
        "description": "The Chevrolet Bolt is an electric hatchback with a long range and practical interior.",
        "year": 2022,
        "manufacturer_id": 19,
        "categories": ["Hatchback", "Electric"],
        "features": ["Regen on Demand", "10.2-Inch Touchscreen", "360-Degree Camera"],
    },
    {
        "name": "Mitsubishi Mirage",
        "description": "The Mitsubishi Mirage is a budget-friendly hatchback with great fuel efficiency.",
        "year": 2020,
        "manufacturer_id": 20,
        "categories": ["Hatchback", "Subcompact"],
        "features": ["Automatic Climate Control", "Keyless Entry", "Hill Start Assist"],
    },
]
