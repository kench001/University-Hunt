# Directive: Research University Data

## Goal
Gather accurate, up-to-date data for Metro Manila universities to populate a comprehensive JSON database.

## Required Fields (per school)
1. **Rank**: Local or national ranking if available (e.g., "#4 in Manila", "Top 10 in PH").
2. **Acceptance Rate**: Estimated percentage (e.g., "12%", "30-40%").
3. **Total Students**: Current enrollment size (e.g., "18,500+", "approx. 10,000").
4. **Website**: Official university website URL.
5. **Tuition**: Accurate tuition range per semester/trimester/quarter.
6. **Featured Programs**: List 5-6 top or flagship academic programs.
7. **Description**: A 2-3 sentence summary of the institution's history and reputation.

## Search Strategy
1. Search for "[University Name] official website".
2. Search for "[University Name] tuition fees 2024 2025".
3. Search for "[University Name] ranking 2024".
4. Search for "[University Name] acceptance rate".
5. Use reputable sources: official university pages, CHED, Edukasyon.ph, FindUniversity.ph.

## Output Format
JSON object containing an array of university data.

## Edge Cases
- **Public Universities**: Mention if tuition is free (RA 10931) but include misc fees.
- **Multiple Campuses**: Focus on the specific campus mentioned in the JSON (e.g., "Main", "Manila", "Diliman").
- **Missing Data**: If specific fields like acceptance rate are not public, provide an "approximate" value based on university selectivity or mark as "Competitive/Selective".
