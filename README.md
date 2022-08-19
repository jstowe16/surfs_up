# surfs_up
## Overview
W. Avy requested weather station data for Oahu in support of securing investment for the surf and ice cream shop. The analysis is performed using SQLite and SQLalchemy, Pandas, Python and the Numpy library. The analysis code is prepared using VS Code (Jupyter Notebook). The precipitation data have been previously issued to W. Avy; this analysis is focused on the temperature data for the months of June and December.

## Results
### June Temperature
The June temperature summary statistics for 2010 to 2017 are provided in the image below.
![image](/Resources/June_temp_stats.png)

### December Temperature
The December temperature summary statistics for 2010 to 2017 are provided in the image below.
![image](/Resources/Dec_temp_stats.png)

### Comparison
The key differences between June and December are:
* The mean temperature for June (74.9°F) is approximately four degrees hotter than for December (71.0°F).
* The minimum temperature in Decmber (56.0°F) is approximately 8 degrees colder than for June (64.0°F).
* There are 1700 temperature observations for June compared to 1517 for December; it is suggested that a sample size sensitivity analysis be completed to ensure representativeness of the results prior to investor commitment. 

## Summary
The June and December tempature observations for 2010 to 2017 are provided for investor information. It is recommended that the data be queried and statistically summarized  for June and December months for temperature at all stations as well as for precipitation at the station of primary interest. 
