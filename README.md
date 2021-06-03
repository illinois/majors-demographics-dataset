# University of Illinois' Enrollment by Curriculum, Race, Sex, Residency 

Data based on student information on Curriculum, Race, Sex and Residency going back to 1967 (where possible). Data aggregated from [DMI](https://www.dmi.illinois.edu/).

## Data Format

The first row of the CSV file contains column headers.  Every row after the first contains data. 

### Course Catalog Data Formats

The course **catalog for 2009-2019 data** (`ethsex0919.csv`) contains one row for each course:

| Term | Year | Term/Year Code | Coll	| Dept | Degree	| Major code | Major Name | Conc code	| Concentration Name (if any) | Total | Men	| Women	| Unknown	| Caucasian	| Asian American	| African American | Hispanic	| Native American	| Hawaiian/Pacific Isl | Multiracial | International | Unknown | All African American | All Native American	| All Hawaiian/ Pac Isl	| All Asian	| Illinois | Non-Illinois	| Academic Program Code |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| Spring	| 2019	| 120191 | KP |	434 |	BS |	0112 | Computer Science | |	| 973 |	681 |	292	| 0	| 256	| 382	| 21 | 43 | 1 | 0 |34 |	221 |	15 | 29 |	5	| 3 |	413 |	502 |	471	| 10KP0112BS |  |
| ... |
| Spring | 2019	| 120191 |	KT |	408 |	BS |	0277 |	Advertising | | | 652	| 207	| 445	| 0	| 428	| 60	| 35	| 55	| 0	| 0	| 24 |	47 | 3	| 43 | 6	| 4	| 77	| 580	| 72	| 10KT0277BS| |
| ... |

Similarly, the course **catalog for all historical data** (`ethsex_all.csv`) contains one row for each course:

**term/year\_code**|**coll**|**dept**|**degree**|**major\_code**|**major\_name**|**conc\_code**|**concentration\_name\_(if\_any)**|**total**|**by\_gender\_men**|**by\_gender\_women**|**by\_gender\_unknown**|**by\_self-reported\_race/ethnicity\_caucasian**|**by\_self-reported\_race/ethnicity\_asian\_american**|**by\_self-reported\_race/ethnicity\_african\_american**|**by\_self-reported\_race/ethnicity\_hispanic**|**by\_self-reported\_race/ethnicity\_native\_american**|**by\_self-reported\_race/ethnicity\_international**|**by\_self-reported\_race/ethnicity\_unknown**|**by\_residency\_illinois**|**by\_residency\_non-illinois**|**academic\_program\_code**|**term**|**year**|**by\_self-reported\_race/ethnicity\_hawaiian/pacific\_isl**|**by\_self-reported\_race/ethnicity\_multiracial**|**all\_students\_including\_multiracial\_and\_hispanic\_all\_african\_american**|**all\_students\_including\_multiracial\_and\_hispanic\_all\_native\_american**|**all\_students\_including\_multiracial\_and\_hispanic\_all\_hawaiian/\_pac\_isl**|**all\_students\_including\_multiracial\_and\_hispanic\_all\_asian**|**by\_self-reported\_race/ethnicity\_all\_african\_american**|**by\_self-reported\_race/ethnicity\_all\_native\_american**|**urm\_urm**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
120071|KL |470|BS |9|Agribusiness, Farm & Financial |10|Agri-Accounting |43|28|15|0|39|2|2|0|0|0|0|43|0|10KL0010BS|sp|7| | | | | | | | | 

 

## Data Source

http://www.dmi.illinois.edu/stuenr/#race
