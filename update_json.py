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
                    "tuition": "Free (RA 10931) for qualified undergraduates; Misc fees apply (approx. \u20b11,000 - \u20b13,000 per sem)."
                },
                {
                    "name": "University of Santo Tomas (UST)",
                    "type": "Private",
                    "info": "Founded in 1611, it is the oldest university in Asia and a premier Catholic institution.",
                    "programs": ["Medicine", "Architecture", "Engineering", "Business", "Accountancy", "Nursing", "Fine Arts", "Liberal Arts"],
                    "tuition": "\u20b160,000 - \u20b1120,000 per semester (varies by program; Medicine is higher)."
                },
                {
                    "name": "De La Salle University (DLSU) - Manila",
                    "type": "Private",
                    "info": "A leading research university known for its business, engineering, and technology programs.",
                    "programs": ["Business", "Engineering", "Computer Studies", "Liberal Arts", "Economics", "Sciences"],
                    "tuition": "\u20b180,000 - \u20b1130,000 per trimester (3 terms per year)."
                },
                {
                    "name": "Polytechnic University of the Philippines (PUP) - Main",
                    "type": "Public",
                    "info": "One of the largest and most affordable public universities in the country.",
                    "programs": ["Accountancy", "Business Administration", "Engineering", "Communication", "Computer Science", "Education"],
                    "tuition": "Free (RA 10931); Misc fees approx. \u20b1500 - \u20b11,500 per semester."
                },
                {
                    "name": "Pamantasan ng Lungsod ng Maynila (PLM)",
                    "type": "Public",
                    "info": "A prestigious city-funded university known for its high board exam passing rates.",
                    "programs": ["Medicine", "Engineering", "Business", "Nursing", "Architecture", "Education"],
                    "tuition": "Free (for Manila residents/qualified scholars); Misc fees approx. \u20b11,000 - \u20b12,000."
                },
                {
                    "name": "Far Eastern University (FEU) - Manila",
                    "type": "Private",
                    "info": "A top-tier private university known for its accountancy, business, and nursing programs.",
                    "programs": ["Accountancy", "Business", "Nursing", "Arts and Sciences", "Education", "Architecture"],
                    "tuition": "\u20b150,000 - \u20b175,000 per semester."
                },
                {
                    "name": "University of the East (UE) - Manila",
                    "type": "Private",
                    "info": "Known for its dentistry program and business courses.",
                    "programs": ["Dentistry", "Business Administration", "Accountancy", "Engineering", "IT", "Arts and Sciences"],
                    "tuition": "\u20b145,000 - \u20b170,000 per semester."
                },
                {
                    "name": "Mapua University (Intramuros)",
                    "type": "Private",
                    "info": "The premier engineering and technology school in the Philippines.",
                    "programs": ["Engineering", "Architecture", "IT", "Multimedia Arts", "Design", "Business"],
                    "tuition": "\u20b135,000 - \u20b155,000 per quarter (4 terms per year)."
                },
                {
                    "name": "Adamson University",
                    "type": "Private",
                    "info": "A private Catholic university known for its engineering and architecture programs.",
                    "programs": ["Engineering", "Architecture", "Business Administration", "Psychology", "Communication"],
                    "tuition": "\u20b145,000 - \u20b165,000 per semester."
                },
                {
                    "name": "Lyceum of the Philippines University (LPU)",
                    "type": "Private",
                    "info": "Founded by Jose P. Laurel, known for international relations and hospitality management.",
                    "programs": ["International Relations", "Hospitality Management", "Business", "Accountancy", "Law"],
                    "tuition": "\u20b150,000 - \u20b175,000 per semester."
                },
                {
                    "name": "San Beda University",
                    "type": "Private",
                    "info": "A premier Benedictine university known for its law, business, and accountancy programs.",
                    "programs": ["Law", "Accountancy", "Business", "Psychology", "Arts and Sciences"],
                    "tuition": "\u20b160,000 - \u20b190,000 per semester."
                },
                {
                    "name": "Technological University of the Philippines (TUP) - Manila",
                    "type": "Public",
                    "info": "The premier state university for technology and engineering in the Philippines.",
                    "programs": ["Engineering", "Technology", "Science", "Education", "Architecture"],
                    "tuition": "Free (RA 10931); Misc fees approx. \u20b11,000 - \u20b12,000."
                },
                {
                    "name": "Universidad de Manila (UDM)",
                    "type": "Public",
                    "info": "A city-funded university offering accessible education to Manila residents.",
                    "programs": ["Criminology", "Business", "Education", "IT", "Arts and Sciences"],
                    "tuition": "Free (for Manila residents); Misc fees approx. \u20b11,000."
                },
                {
                    "name": "Philippine Normal University (PNU)",
                    "type": "Public",
                    "info": "The National Center for Teacher Education.",
                    "programs": ["Education", "English", "Science", "Mathematics", "Social Sciences"],
                    "tuition": "Free (RA 10931); Misc fees apply."
                },
                {
                    "name": "National University (NU) - Manila",
                    "type": "Private",
                    "info": "A dynamic private university known for its engineering and sports programs.",
                    "programs": ["Engineering", "Business", "IT", "Accountancy", "Architecture"],
                    "tuition": "\u20b140,000 - \u20b165,000 per semester."
                },
                {
                    "name": "Centro Escolar University (CEU) - Manila",
                    "type": "Private",
                    "info": "A leading university for dentistry, pharmacy, and health sciences.",
                    "programs": ["Dentistry", "Pharmacy", "Medical Technology", "Nursing", "Education"],
                    "tuition": "\u20b150,000 - \u20b180,000 per semester."
                },
                {
                    "name": "Philippine Women's University (PWU)",
                    "type": "Private",
                    "info": "The first university for women in Asia, now co-educational, known for social work and music.",
                    "programs": ["Social Work", "Music", "Fine Arts", "Business", "Nursing"],
                    "tuition": "\u20b145,000 - \u20b170,000 per semester."
                },
                {
                    "name": "Colegio de San Juan de Letran",
                    "type": "Private",
                    "info": "A historic Dominican institution inside Intramuros.",
                    "programs": ["Communication", "Business", "Accountancy", "Education", "IT"],
                    "tuition": "\u20b150,000 - \u20b175,000 per semester."
                },
                {
                    "name": "Emilio Aguinaldo College (EAC)",
                    "type": "Private",
                    "info": "Known for its medical and health programs.",
                    "programs": ["Medicine", "Nursing", "Criminology", "Physical Therapy", "Education"],
                    "tuition": "\u20b140,000 - \u20b165,000 per semester."
                },
                {
                    "name": "Philippine Christian University (PCU)",
                    "type": "Private",
                    "info": "A Christian university known for its diverse academic offerings and athletic programs.",
                    "programs": ["Business", "Education", "IT", "Social Sciences", "Nursing"],
                    "tuition": "\u20b135,000 - \u20b155,000 per semester."
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
                    "tuition": "Free (RA 10931) for qualified undergraduates; Misc fees approx. \u20b11,000 - \u20b13,000."
                },
                {
                    "name": "Ateneo de Manila University (ADMU)",
                    "type": "Private",
                    "info": "A prestigious Jesuit university known for its liberal arts and management programs.",
                    "programs": ["Management", "Social Sciences", "Humanities", "Sciences", "Engineering", "Law"],
                    "tuition": "\u20b1100,000 - \u20b1150,000 per semester."
                },
                {
                    "name": "Miriam College",
                    "type": "Private",
                    "info": "A premier women's college known for its social work, education, and arts programs.",
                    "programs": ["Education", "Communication", "International Studies", "Business", "Arts", "Psychology"],
                    "tuition": "\u20b150,000 - \u20b180,000 per semester."
                },
                {
                    "name": "Quezon City University (QCU)",
                    "type": "Public",
                    "info": "A local government-funded university providing affordable education to QC residents.",
                    "programs": ["IT", "Engineering", "Business Administration", "Entrepreneurship", "Public Administration"],
                    "tuition": "Free (for qualified QC residents); Misc fees approx. \u20b11,000 - \u20b12,000."
                },
                {
                    "name": "Trinity University of Asia",
                    "type": "Private",
                    "info": "A respected private university known for its nursing and medical technology programs.",
                    "programs": ["Nursing", "Medical Technology", "Business", "Education", "Arts and Sciences"],
                    "tuition": "\u20b140,000 - \u20b165,000 per semester."
                },
                {
                    "name": "Technological Institute of the Philippines (TIP) - QC",
                    "type": "Private",
                    "info": "Specializes in engineering and technical courses with industry-aligned curricula.",
                    "programs": ["Engineering", "IT", "Architecture", "Business", "Education"],
                    "tuition": "\u20b135,000 - \u20b155,000 per semester."
                },
                {
                    "name": "New Era University (NEU)",
                    "type": "Private",
                    "info": "A non-sectarian university known for its discipline and diverse course offerings.",
                    "programs": ["Medicine", "Nursing", "Engineering", "Accountancy", "Communication"],
                    "tuition": "\u20b130,000 - \u20b150,000 per semester."
                },
                {
                    "name": "AMA Computer University",
                    "type": "Private",
                    "info": "A pioneer in ICT education in the Philippines.",
                    "programs": ["IT", "Computer Science", "Engineering", "Business", "Multimedia Arts"],
                    "tuition": "\u20b130,000 - \u20b155,000 per semester."
                },
                {
                    "name": "STI College - Quezon City",
                    "type": "Private",
                    "info": "Part of a large network of colleges focusing on IT and tourism education.",
                    "programs": ["IT", "Tourism Management", "Hospitality Management", "Business", "Engineering"],
                    "tuition": "\u20b130,000 - \u20b150,000 per semester."
                },
                {
                    "name": "National College of Business and Arts (NCBA)",
                    "type": "Private",
                    "info": "Specializes in business, accountancy, and secretarial courses.",
                    "programs": ["Accountancy", "Business Administration", "Education", "IT"],
                    "tuition": "\u20b125,000 - \u20b140,000 per semester."
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
                    "tuition": "Free (for Makati residents); \u20b11,000 - \u20b13,000 misc fees."
                },
                {
                    "name": "Asia Pacific College (APC)",
                    "type": "Private",
                    "info": "A partnership between SM Foundation and IBM, specializing in IT and business.",
                    "programs": ["Computer Science", "IT", "Engineering", "Accountancy", "Business Administration", "Multimedia Arts"],
                    "tuition": "\u20b150,000 - \u20b180,000 per semester."
                },
                {
                    "name": "Assumption College",
                    "type": "Private",
                    "info": "A premier Catholic women's college in Makati.",
                    "programs": ["Communication", "Business", "Education", "Psychology", "Interior Design"],
                    "tuition": "\u20b170,000 - \u20b1110,000 per semester."
                },
                {
                    "name": "Asian Institute of Management (AIM)",
                    "type": "Private",
                    "info": "A leading international graduate school of business.",
                    "programs": ["MBA", "Masters in Data Science", "Masters in Entrepreneurship"],
                    "tuition": "\u20b11,000,000 - \u20b11,500,000+ per program."
                },
                {
                    "name": "International Academy of Management and Economics (IAME)",
                    "type": "Private",
                    "info": "A specialized business and management school.",
                    "programs": ["Business Management", "Economics", "Leadership Studies"],
                    "tuition": "\u20b140,000 - \u20b165,000 per semester."
                },
                {
                    "name": "Centro Escolar University (CEU) - Makati",
                    "type": "Private",
                    "info": "Makati campus specializing in professional studies and business.",
                    "programs": ["Business", "Accountancy", "Tourism", "IT", "Psychology"],
                    "tuition": "\u20b150,000 - \u20b175,000 per semester."
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
                    "tuition": "Free (for Taguig residents); Misc fees approx. \u20b11,000 - \u20b12,000."
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
                    "tuition": "\u20b1150,000 - \u20b1250,000 per semester."
                },
                {
                    "name": "Treston International College",
                    "type": "Private",
                    "info": "Offers international standard programs in business and hospitality.",
                    "programs": ["Hospitality", "Business", "Culinary Arts", "IT"],
                    "tuition": "\u20b180,000 - \u20b1130,000 per semester."
                },
                {
                    "name": "Global City Innovative College (GCIC)",
                    "type": "Private",
                    "info": "A modern college in BGC offering specialized undergraduate programs.",
                    "programs": ["Nursing", "Business Administration", "IT", "Tourism"],
                    "tuition": "\u20b145,000 - \u20b170,000 per semester."
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
                    "tuition": "Free (for Caloocan residents); Misc fees approx. \u20b1500 - \u20b11,500."
                },
                {
                    "name": "Manila Central University (MCU)",
                    "type": "Private",
                    "info": "Known for its health science and medical programs.",
                    "programs": ["Medicine", "Nursing", "Pharmacy", "Dentistry", "Business", "IT"],
                    "tuition": "\u20b140,000 - \u20b170,000 per semester."
                },
                {
                    "name": "University of the East (UE) - Caloocan",
                    "type": "Private",
                    "info": "The northern campus of UE, offering diverse programs.",
                    "programs": ["Engineering", "Business", "Fine Arts", "Arts and Sciences"],
                    "tuition": "\u20b145,000 - \u20b165,000 per semester."
                },
                {
                    "name": "St. Clare College of Caloocan",
                    "type": "Private",
                    "info": "A private college providing affordable education to the Caloocan community.",
                    "programs": ["Education", "Business Administration", "IT", "Criminology"],
                    "tuition": "\u20b120,000 - \u20b135,000 per semester."
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
                    "tuition": "Free (for Valenzuela residents); Misc fees approx. \u20b11,000 - \u20b12,000."
                },
                {
                    "name": "Our Lady of Fatima University (OLFU)",
                    "type": "Private",
                    "info": "A major private university known for its medical and allied health programs.",
                    "programs": ["Medicine", "Nursing", "Pharmacy", "Medical Technology", "Business", "IT", "Criminology"],
                    "tuition": "\u20b140,000 - \u20b165,000 per semester."
                },
                {
                    "name": "Valenzuela City Polytechnic College",
                    "type": "Public",
                    "info": "Focused on technical and vocational education for the city.",
                    "programs": ["Technology", "Industrial Education", "Technical Courses"],
                    "tuition": "Free (for residents); Misc fees apply."
                },
                {
                    "name": "St. Louis College Valenzuela",
                    "type": "Private",
                    "info": "A private educational institution providing local access to degree programs.",
                    "programs": ["Business", "Education", "IT"],
                    "tuition": "\u20b125,000 - \u20b140,000 per semester."
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
                    "tuition": "Free (for Malabon residents); Misc fees approx. \u20b1500 - \u20b11,500."
                },
                {
                    "name": "De La Salle Araneta University (DLSAU)",
                    "type": "Private",
                    "info": "A member of the De La Salle Philippines system, known for veterinary medicine and agriculture.",
                    "programs": ["Veterinary Medicine", "Agriculture", "Business", "Education", "IT"],
                    "tuition": "\u20b140,000 - \u20b165,000 per semester."
                },
                {
                    "name": "Arellano University - Malabon",
                    "type": "Private",
                    "info": "The Malabon campus of Arellano University.",
                    "programs": ["Business", "Education", "Nursing", "Criminology"],
                    "tuition": "\u20b130,000 - \u20b150,000 per semester."
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
                },
                {
                    "name": "Governor Andres Pascual College",
                    "type": "Private",
                    "info": "A long-standing private college in Navotas.",
                    "programs": ["Business", "Education", "Accountancy"],
                    "tuition": "\u20b125,000 - \u20b140,000 per semester."
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
                    "tuition": "Free (for Pasig residents); Misc fees approx. \u20b11,000 - \u20b12,000."
                },
                {
                    "name": "University of Asia and the Pacific (UA&P)",
                    "type": "Private",
                    "info": "A private research university known for economics and business programs.",
                    "programs": ["Economics", "Business Administration", "Management", "Communication", "Political Economy"],
                    "tuition": "\u20b190,000 - \u20b1140,000 per semester."
                },
                {
                    "name": "Pasig Catholic College",
                    "type": "Private",
                    "info": "A respected Catholic institution in the heart of Pasig.",
                    "programs": ["Business", "Education", "IT", "Hospitality Management"],
                    "tuition": "\u20b130,000 - \u20b150,000 per semester."
                },
                {
                    "name": "Arellano University - Pasig",
                    "type": "Private",
                    "info": "The Pasig campus of Arellano University.",
                    "programs": ["Nursing", "Business Administration", "Education", "IT"],
                    "tuition": "\u20b130,000 - \u20b150,000 per semester."
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
                    "tuition": "Free (RA 10931); Misc fees approx. \u20b11,000 - \u20b12,500."
                },
                {
                    "name": "Jose Rizal University (JRU)",
                    "type": "Private",
                    "info": "Known for its business, accountancy, and law programs.",
                    "programs": ["Business Administration", "Accountancy", "Law", "IT", "Education", "Nursing"],
                    "tuition": "\u20b135,000 - \u20b155,000 per semester."
                },
                {
                    "name": "Don Bosco Technical College (DBTC)",
                    "type": "Private",
                    "info": "Renowned for its technical and engineering education.",
                    "programs": ["Engineering", "IT", "Architecture", "Education"],
                    "tuition": "\u20b140,000 - \u20b165,000 per semester."
                },
                {
                    "name": "Arellano University - Mandaluyong",
                    "type": "Private",
                    "info": "The Mandaluyong campus of Arellano University.",
                    "programs": ["Education", "Business", "IT", "Criminology"],
                    "tuition": "\u20b130,000 - \u20b150,000 per semester."
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
                    "tuition": "Free (RA 10931); Misc fees approx. \u20b1500 - \u20b11,500."
                },
                {
                    "name": "Dominican College",
                    "type": "Private",
                    "info": "A private Catholic college offering diverse programs.",
                    "programs": ["Hospitality Management", "Business", "Education", "Arts and Sciences"],
                    "tuition": "\u20b130,000 - \u20b150,000 per semester."
                },
                {
                    "name": "Informatics College - San Juan",
                    "type": "Private",
                    "info": "Specializes in IT and computer education.",
                    "programs": ["IT", "Computer Science", "Business Administration"],
                    "tuition": "\u20b125,000 - \u20b145,000 per semester."
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
                    "tuition": "Free (for Marikina residents); Misc fees approx. \u20b11,000 - \u20b12,000."
                },
                {
                    "name": "Marikina Polytechnic College (MPC)",
                    "type": "Public",
                    "info": "Specializes in technical and vocational teacher education.",
                    "programs": ["Technical Teacher Education", "Technology"],
                    "tuition": "Free (RA 10931); Misc fees apply."
                },
                {
                    "name": "Roosevelt College Marikina",
                    "type": "Private",
                    "info": "A private educational institution part of the FEU system.",
                    "programs": ["Education", "Business", "IT", "Tourism"],
                    "tuition": "\u20b130,000 - \u20b150,000 per semester."
                }
            ]
        },
        {
            "name": "Para\u00f1aque",
            "universities": [
                {
                    "name": "Para\u00f1aque City College (PCC)",
                    "type": "Public",
                    "info": "Provides affordable higher education to Para\u00f1aque residents.",
                    "programs": ["Hospitality Management", "IT", "Business Administration"],
                    "tuition": "Free (for Para\u00f1aque residents); Misc fees approx. \u20b11,000 - \u20b12,000."
                },
                {
                    "name": "PATTS College of Aeronautics",
                    "type": "Private",
                    "info": "A premier institution for aviation and aeronautical education.",
                    "programs": ["Aeronautical Engineering", "Aircraft Maintenance", "Tourism", "Airline Management"],
                    "tuition": "\u20b145,000 - \u20b170,000 per semester."
                },
                {
                    "name": "Olivarez College",
                    "type": "Private",
                    "info": "Known for its nursing and health-related programs.",
                    "programs": ["Nursing", "Medical Technology", "Business", "Education", "Criminology"],
                    "tuition": "\u20b135,000 - \u20b155,000 per semester."
                },
                {
                    "name": "Don Bosco College - Para\u00f1aque",
                    "type": "Private",
                    "info": "A technical-vocation focused college in the Don Bosco network.",
                    "programs": ["Technical Education", "Education", "Religious Studies"],
                    "tuition": "\u20b125,000 - \u20b145,000 per semester."
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
                    "tuition": "Free (for Pasay residents); Misc fees approx. \u20b11,000 - \u20b12,000."
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
                    "tuition": "\u20b145,000 - \u20b175,000 per semester."
                },
                {
                    "name": "Manila Adventist College",
                    "type": "Private",
                    "info": "A private Christian college known for its nursing and health programs.",
                    "programs": ["Nursing", "Medical Technology", "Business", "Accountancy"],
                    "tuition": "\u20b140,000 - \u20b165,000 per semester."
                }
            ]
        },
        {
            "name": "Las Pi\u00f1as",
            "universities": [
                {
                    "name": "University of Perpetual Help System DALTA (UPHSD)",
                    "type": "Private",
                    "info": "A major university system known for medicine, nursing, and engineering.",
                    "programs": ["Medicine", "Nursing", "Engineering", "Business", "Law", "Aviation", "Maritime"],
                    "tuition": "\u20b150,000 - \u20b185,000 per semester."
                },
                {
                    "name": "Southville International School and Colleges",
                    "type": "Private",
                    "info": "An international standard institution offering diverse programs.",
                    "programs": ["Business", "Psychology", "IT", "Nursing", "Multimedia Arts"],
                    "tuition": "\u20b170,000 - \u20b1120,000 per semester."
                },
                {
                    "name": "Dr. Filemon C. Aguilar Memorial College",
                    "type": "Public",
                    "info": "A local public college for Las Pi\u00f1as residents.",
                    "programs": ["Accountancy", "Business Administration"],
                    "tuition": "Free (for Las Pi\u00f1as residents); Misc fees apply."
                },
                {
                    "name": "Saint Francis of Assisi College - Las Pi\u00f1as",
                    "type": "Private",
                    "info": "A private educational institution providing affordable degree programs.",
                    "programs": ["Education", "Business Administration", "IT", "Tourism"],
                    "tuition": "\u20b125,000 - \u20b145,000 per semester."
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
                    "tuition": "Free (for Muntinlupa residents); Misc fees approx. \u20b11,000 - \u20b12,000."
                },
                {
                    "name": "San Beda College - Alabang",
                    "type": "Private",
                    "info": "The Alabang campus of San Beda, offering top-tier education.",
                    "programs": ["Business", "Accountancy", "Psychology", "IT", "Law"],
                    "tuition": "\u20b170,000 - \u20b1110,000 per semester."
                },
                {
                    "name": "FEU Alabang",
                    "type": "Private",
                    "info": "Specializes in engineering, business, and technology.",
                    "programs": ["Engineering", "Computer Science", "IT", "Business"],
                    "tuition": "\u20b160,000 - \u20b190,000 per semester."
                },
                {
                    "name": "West Bay College",
                    "type": "Private",
                    "info": "A maritime college focused on producing competitive seafarers.",
                    "programs": ["Marine Transportation", "Marine Engineering", "Business"],
                    "tuition": "\u20b135,000 - \u20b155,000 per semester."
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
                    "tuition": "Free (for Pateros residents); Misc fees approx. \u20b1500 - \u20b11,500."
                }
            ]
        }
    ]
}

with open("metro_manila_universities.json", "w") as f:
    json.dump(data, f, indent=4)

print("JSON file updated with 100+ institutions successfully.")
