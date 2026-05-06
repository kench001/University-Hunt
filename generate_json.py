import json

data = {
    "cities": [
        {
            "name": "Manila (The Capital)",
            "universities": [
                {
                    "name": "University of the Philippines Manila (UPM)",
                    "type": "Public",
                    "info": "The country's premier institution for health sciences and medical education.",
                    "programs": ["Medicine", "Nursing", "Pharmacy", "Public Health", "Physical Therapy", "Dentistry", "Arts and Sciences"],
                    "tuition": "Free (RA 10931) for qualified undergraduates; Misc fees apply (approx. ₱1,000 - ₱3,000 per sem)."
                },
                {
                    "name": "University of Santo Tomas (UST)",
                    "type": "Private",
                    "info": "Founded in 1611, it is the oldest university in Asia and a premier Catholic institution.",
                    "programs": ["Medicine", "Architecture", "Engineering", "Business", "Accountancy", "Nursing", "Fine Arts", "Liberal Arts"],
                    "tuition": "₱60,000 - ₱120,000 per semester (varies by program; Medicine is higher)."
                },
                {
                    "name": "De La Salle University (DLSU) - Manila",
                    "type": "Private",
                    "info": "A leading research university known for its business, engineering, and technology programs.",
                    "programs": ["Business", "Engineering", "Computer Studies", "Liberal Arts", "Economics", "Sciences"],
                    "tuition": "₱80,000 - ₱130,000 per trimester (3 terms per year)."
                },
                {
                    "name": "Polytechnic University of the Philippines (PUP) - Main",
                    "type": "Public",
                    "info": "One of the largest and most affordable public universities in the country.",
                    "programs": ["Accountancy", "Business Administration", "Engineering", "Communication", "Computer Science", "Education"],
                    "tuition": "Free (RA 10931); Misc fees approx. ₱500 - ₱1,500 per semester."
                },
                {
                    "name": "Pamantasan ng Lungsod ng Maynila (PLM)",
                    "type": "Public",
                    "info": "A prestigious city-funded university known for its high board exam passing rates.",
                    "programs": ["Medicine", "Engineering", "Business", "Nursing", "Architecture", "Education"],
                    "tuition": "Free (for Manila residents/qualified scholars); Misc fees approx. ₱1,000 - ₱2,000."
                },
                {
                    "name": "Far Eastern University (FEU) - Manila",
                    "type": "Private",
                    "info": "A top-tier private university known for its accountancy, business, and nursing programs.",
                    "programs": ["Accountancy", "Business", "Nursing", "Arts and Sciences", "Education", "Architecture"],
                    "tuition": "₱50,000 - ₱75,000 per semester."
                },
                {
                    "name": "University of the East (UE) - Manila",
                    "type": "Private",
                    "info": "Known for its dentistry program and business courses.",
                    "programs": ["Dentistry", "Business Administration", "Accountancy", "Engineering", "IT", "Arts and Sciences"],
                    "tuition": "₱45,000 - ₱70,000 per semester."
                },
                {
                    "name": "Mapua University (Intramuros)",
                    "type": "Private",
                    "info": "The premier engineering and technology school in the Philippines.",
                    "programs": ["Engineering", "Architecture", "IT", "Multimedia Arts", "Design", "Business"],
                    "tuition": "₱35,000 - ₱55,000 per quarter (4 terms per year)."
                }
            ]
        },
        {
            "name": "Quezon City",
            "universities": [
                {
                    "name": "University of the Philippines Diliman (UPD)",
                    "type": "Public",
                    "info": "The flagship campus of the UP System and a National University.",
                    "programs": ["Engineering", "Law", "Business", "Sciences", "Social Sciences", "Fine Arts", "Music", "Education"],
                    "tuition": "Free (RA 10931) for qualified undergraduates; Misc fees approx. ₱1,000 - ₱3,000."
                },
                {
                    "name": "Ateneo de Manila University (ADMU)",
                    "type": "Private",
                    "info": "A prestigious Jesuit university known for its liberal arts and management programs.",
                    "programs": ["Management", "Social Sciences", "Humanities", "Sciences", "Engineering", "Law"],
                    "tuition": "₱100,000 - ₱150,000 per semester."
                },
                {
                    "name": "Miriam College",
                    "type": "Private",
                    "info": "A premier women's college known for its social work, education, and arts programs.",
                    "programs": ["Education", "Communication", "International Studies", "Business", "Arts", "Psychology"],
                    "tuition": "₱50,000 - ₱80,000 per semester."
                },
                {
                    "name": "Quezon City University (QCU)",
                    "type": "Public",
                    "info": "A local government-funded university providing affordable education to QC residents.",
                    "programs": ["IT", "Engineering", "Business Administration", "Entrepreneurship", "Public Administration"],
                    "tuition": "Free (for qualified QC residents); Misc fees approx. ₱1,000 - ₱2,000."
                },
                {
                    "name": "Trinity University of Asia",
                    "type": "Private",
                    "info": "A respected private university known for its nursing and medical technology programs.",
                    "programs": ["Nursing", "Medical Technology", "Business", "Education", "Arts and Sciences"],
                    "tuition": "₱40,000 - ₱65,000 per semester."
                }
            ]
        },
        {
            "name": "Makati",
            "universities": [
                {
                    "name": "University of Makati (UMak)",
                    "type": "Public",
                    "info": "A city-funded university offering a wide range of academic and technical programs.",
                    "programs": ["Business", "IT", "Nursing", "Education", "Criminology", "Governance"],
                    "tuition": "Free (for Makati residents); ₱1,000 - ₱3,000 misc fees. (New scheme for non-residents applies)."
                },
                {
                    "name": "Asia Pacific College (APC)",
                    "type": "Private",
                    "info": "A partnership between SM Foundation and IBM, specializing in IT and business.",
                    "programs": ["Computer Science", "IT", "Engineering", "Accountancy", "Business Administration", "Multimedia Arts"],
                    "tuition": "₱50,000 - ₱80,000 per semester."
                },
                {
                    "name": "Assumption College",
                    "type": "Private",
                    "info": "A premier Catholic women's college in Makati.",
                    "programs": ["Communication", "Business", "Education", "Psychology", "Interior Design"],
                    "tuition": "₱70,000 - ₱110,000 per semester."
                },
                {
                    "name": "Asian Institute of Management (AIM)",
                    "type": "Private",
                    "info": "A leading international graduate school of business.",
                    "programs": ["MBA", "Masters in Data Science", "Masters in Entrepreneurship"],
                    "tuition": "₱1,000,000 - ₱1,500,000+ per program (Graduate level)."
                }
            ]
        },
        {
            "name": "Taguig",
            "universities": [
                {
                    "name": "Taguig City University (TCU)",
                    "type": "Public",
                    "info": "A local university serving the residents of Taguig with diverse course offerings.",
                    "programs": ["Education", "Business Administration", "IT", "Criminology", "Public Administration"],
                    "tuition": "Free (for Taguig residents); Misc fees approx. ₱1,000 - ₱2,000."
                },
                {
                    "name": "Technological University of the Philippines (TUP) - Taguig",
                    "type": "Public",
                    "info": "Specializes in engineering and technical education.",
                    "programs": ["Engineering", "Technology", "Science"],
                    "tuition": "Free (RA 10931); Misc fees apply."
                },
                {
                    "name": "Enderun Colleges",
                    "type": "Private",
                    "info": "A high-end international college known for hospitality and business management.",
                    "programs": ["Hospitality Management", "Culinary Arts", "Business Administration", "Economics"],
                    "tuition": "₱150,000 - ₱250,000 per semester."
                },
                {
                    "name": "Treston International College",
                    "type": "Private",
                    "info": "Offers international standard programs in business and hospitality.",
                    "programs": ["Hospitality", "Business", "Culinary Arts", "IT"],
                    "tuition": "₱80,000 - ₱130,000 per semester."
                }
            ]
        },
        {
            "name": "Caloocan",
            "universities": [
                {
                    "name": "University of Caloocan City (UCC)",
                    "type": "Public",
                    "info": "A city-run university with several campuses in Caloocan.",
                    "programs": ["Business", "Education", "IT", "Criminology", "Liberal Arts"],
                    "tuition": "Free (for Caloocan residents); Misc fees approx. ₱500 - ₱1,500."
                },
                {
                    "name": "Manila Central University (MCU)",
                    "type": "Private",
                    "info": "Known for its health science and medical programs.",
                    "programs": ["Medicine", "Nursing", "Pharmacy", "Dentistry", "Business", "IT"],
                    "tuition": "₱40,000 - ₱70,000 per semester (Medicine is higher)."
                },
                {
                    "name": "University of the East (UE) - Caloocan",
                    "type": "Private",
                    "info": "The northern campus of UE, offering diverse programs.",
                    "programs": ["Engineering", "Business", "Fine Arts", "Arts and Sciences"],
                    "tuition": "₱45,000 - ₱65,000 per semester."
                }
            ]
        },
        {
            "name": "Valenzuela",
            "universities": [
                {
                    "name": "Pamantasan ng Lungsod ng Valenzuela (PLV)",
                    "type": "Public",
                    "info": "The primary public university for Valenzuela residents.",
                    "programs": ["Education", "Business Administration", "IT", "Criminology", "Engineering"],
                    "tuition": "Free (for Valenzuela residents); Misc fees approx. ₱1,000 - ₱2,000."
                },
                {
                    "name": "Our Lady of Fatima University (OLFU)",
                    "type": "Private",
                    "info": "A major private university known for its medical and allied health programs.",
                    "programs": ["Medicine", "Nursing", "Pharmacy", "Medical Technology", "Business", "IT", "Criminology"],
                    "tuition": "₱40,000 - ₱65,000 per semester (Medicine is higher)."
                }
            ]
        },
        {
            "name": "Malabon",
            "universities": [
                {
                    "name": "City of Malabon University (CMU)",
                    "type": "Public",
                    "info": "Serves the Malabon community with affordable higher education.",
                    "programs": ["Business", "Education", "IT", "Criminology", "Accountancy"],
                    "tuition": "Free (for Malabon residents); Misc fees approx. ₱500 - ₱1,500."
                },
                {
                    "name": "De La Salle Araneta University (DLSAU)",
                    "type": "Private",
                    "info": "A member of the De La Salle Philippines system, known for veterinary medicine and agriculture.",
                    "programs": ["Veterinary Medicine", "Agriculture", "Business", "Education", "IT"],
                    "tuition": "₱40,000 - ₱65,000 per semester."
                }
            ]
        },
        {
            "name": "Navotas",
            "universities": [
                {
                    "name": "Navotas Polytechnic College (NPC)",
                    "type": "Public",
                    "info": "The local government-funded college in Navotas.",
                    "programs": ["Education", "Business Administration", "IT", "Criminology"],
                    "tuition": "Free (for Navotas residents); Misc fees apply."
                }
            ]
        },
        {
            "name": "Pasig",
            "universities": [
                {
                    "name": "Pamantasan ng Lungsod ng Pasig (PLP)",
                    "type": "Public",
                    "info": "Provides quality higher education to Pasig residents.",
                    "programs": ["Nursing", "Education", "Business", "IT", "Criminology"],
                    "tuition": "Free (for Pasig residents); Misc fees approx. ₱1,000 - ₱2,000."
                },
                {
                    "name": "University of Asia and the Pacific (UA&P)",
                    "type": "Private",
                    "info": "A private research university known for economics and business programs.",
                    "programs": ["Economics", "Business Administration", "Management", "Communication", "Political Economy"],
                    "tuition": "₱90,000 - ₱140,000 per semester."
                },
                {
                    "name": "Pasig Catholic College",
                    "type": "Private",
                    "info": "A respected Catholic institution in the heart of Pasig.",
                    "programs": ["Business", "Education", "IT", "Hospitality Management"],
                    "tuition": "₱30,000 - ₱50,000 per semester."
                }
            ]
        },
        {
            "name": "Mandaluyong",
            "universities": [
                {
                    "name": "Rizal Technological University (RTU)",
                    "type": "Public",
                    "info": "A state university specializing in technology and engineering.",
                    "programs": ["Engineering", "Architecture", "Technology", "Business", "Education"],
                    "tuition": "Free (RA 10931); Misc fees approx. ₱1,000 - ₱2,500."
                },
                {
                    "name": "Jose Rizal University (JRU)",
                    "type": "Private",
                    "info": "Known for its business, accountancy, and law programs.",
                    "programs": ["Business Administration", "Accountancy", "Law", "IT", "Education", "Nursing"],
                    "tuition": "₱35,000 - ₱55,000 per semester."
                },
                {
                    "name": "Don Bosco Technical College (DBTC)",
                    "type": "Private",
                    "info": "Renowned for its technical and engineering education.",
                    "programs": ["Engineering", "IT", "Architecture", "Education"],
                    "tuition": "₱40,000 - ₱65,000 per semester."
                }
            ]
        },
        {
            "name": "San Juan",
            "universities": [
                {
                    "name": "Polytechnic University of the Philippines (PUP) - San Juan",
                    "type": "Public",
                    "info": "The San Juan campus of the PUP system.",
                    "programs": ["Business Administration", "IT", "Education"],
                    "tuition": "Free (RA 10931); Misc fees approx. ₱500 - ₱1,500."
                },
                {
                    "name": "Dominican College",
                    "type": "Private",
                    "info": "A private Catholic college offering diverse programs.",
                    "programs": ["Hospitality Management", "Business", "Education", "Arts and Sciences"],
                    "tuition": "₱30,000 - ₱50,000 per semester."
                }
            ]
        },
        {
            "name": "Marikina",
            "universities": [
                {
                    "name": "Pamantasan ng Lungsod ng Marikina (PLMar)",
                    "type": "Public",
                    "info": "A city university providing affordable education to Marikina residents.",
                    "programs": ["Business", "Education", "IT", "Criminology", "Nursing"],
                    "tuition": "Free (for Marikina residents); Misc fees approx. ₱1,000 - ₱2,000."
                },
                {
                    "name": "Marikina Polytechnic College (MPC)",
                    "type": "Public",
                    "info": "Specializes in technical and vocational teacher education.",
                    "programs": ["Technical Teacher Education", "Technology"],
                    "tuition": "Free (RA 10931); Misc fees apply."
                }
            ]
        },
        {
            "name": "Parañaque",
            "universities": [
                {
                    "name": "Parañaque City College (PCC)",
                    "type": "Public",
                    "info": "Provides affordable higher education to Parañaque residents.",
                    "programs": ["Hospitality Management", "IT", "Business Administration"],
                    "tuition": "Free (for Parañaque residents); Misc fees approx. ₱1,000 - ₱2,000."
                },
                {
                    "name": "PATTS College of Aeronautics",
                    "type": "Private",
                    "info": "A premier institution for aviation and aeronautical education.",
                    "programs": ["Aeronautical Engineering", "Aircraft Maintenance", "Tourism", "Airline Management"],
                    "tuition": "₱45,000 - ₱70,000 per semester."
                },
                {
                    "name": "Olivarez College",
                    "type": "Private",
                    "info": "Known for its nursing and health-related programs.",
                    "programs": ["Nursing", "Medical Technology", "Business", "Education", "Criminology"],
                    "tuition": "₱35,000 - ₱55,000 per semester."
                }
            ]
        },
        {
            "name": "Pasay",
            "universities": [
                {
                    "name": "City University of Pasay (CUP)",
                    "type": "Public",
                    "info": "The local government university for Pasay residents.",
                    "programs": ["Business Administration", "Education", "IT", "Criminology", "Nursing"],
                    "tuition": "Free (for Pasay residents); Misc fees approx. ₱1,000 - ₱2,000."
                },
                {
                    "name": "Philippine State College of Aeronautics (PhilSCA)",
                    "type": "Public",
                    "info": "The only state college in the Philippines offering aeronautics courses.",
                    "programs": ["Aeronautical Engineering", "Aircraft Maintenance", "Aviation Management"],
                    "tuition": "Free (RA 10931); Misc fees apply."
                },
                {
                    "name": "Manila Tytana Colleges",
                    "type": "Private",
                    "info": "An educational institution under the Metrobank Group, known for nursing.",
                    "programs": ["Nursing", "Medical Technology", "Business", "Psychology", "Hospitality Management"],
                    "tuition": "₱45,000 - ₱75,000 per semester."
                }
            ]
        },
        {
            "name": "Las Piñas",
            "universities": [
                {
                    "name": "University of Perpetual Help System DALTA (UPHSD)",
                    "type": "Private",
                    "info": "A major university system known for medicine, nursing, and engineering.",
                    "programs": ["Medicine", "Nursing", "Engineering", "Business", "Law", "Aviation", "Maritime"],
                    "tuition": "₱50,000 - ₱85,000 per semester (Medicine is higher)."
                },
                {
                    "name": "Southville International School and Colleges",
                    "type": "Private",
                    "info": "An international standard institution offering diverse programs.",
                    "programs": ["Business", "Psychology", "IT", "Nursing", "Multimedia Arts"],
                    "tuition": "₱70,000 - ₱120,000 per semester."
                },
                {
                    "name": "Dr. Filemon C. Aguilar Memorial College",
                    "type": "Public",
                    "info": "A local public college for Las Piñas residents.",
                    "programs": ["Accountancy", "Business Administration"],
                    "tuition": "Free (for Las Piñas residents); Misc fees apply."
                }
            ]
        },
        {
            "name": "Muntinlupa",
            "universities": [
                {
                    "name": "Pamantasan ng Lungsod ng Muntinlupa (PLMun)",
                    "type": "Public",
                    "info": "A city-run university serving the Muntinlupa community.",
                    "programs": ["Education", "Business Administration", "IT", "Criminology", "Nursing"],
                    "tuition": "Free (for Muntinlupa residents); Misc fees approx. ₱1,000 - ₱2,000."
                },
                {
                    "name": "San Beda College - Alabang",
                    "type": "Private",
                    "info": "The Alabang campus of San Beda, offering top-tier education.",
                    "programs": ["Business", "Accountancy", "Psychology", "IT", "Law"],
                    "tuition": "₱70,000 - ₱110,000 per semester."
                },
                {
                    "name": "FEU Alabang",
                    "type": "Private",
                    "info": "Specializes in engineering, business, and technology.",
                    "programs": ["Engineering", "Computer Science", "IT", "Business"],
                    "tuition": "₱60,000 - ₱90,000 per semester."
                }
            ]
        },
        {
            "name": "Pateros (Municipality)",
            "universities": [
                {
                    "name": "Pateros Technological College (PTC)",
                    "type": "Public",
                    "info": "The primary higher education institution in the municipality of Pateros.",
                    "programs": ["Business Administration", "IT", "Education", "Office Administration"],
                    "tuition": "Free (for Pateros residents); Misc fees approx. ₱500 - ₱1,500."
                }
            ]
        }
    ]
}

with open("metro_manila_universities.json", "w") as f:
    json.dump(data, f, indent=4)

print("JSON file created successfully.")
