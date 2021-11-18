# Practice Plot
Practice plotting data using Python.

## Libraries
- Numpy
- Matplotlib

## Data
Data is taken from IPCC (The Intergovernmental Panel on Climate Change).
The main site is https://www.ipcc.ch/

Observation data is taken from https://ipcc-data.org/observ/index.html, specifically from this Excel workbook: "WG1AR5_AIISM_Datafiles.xlsx".

List of all tables:
- Table AII.1.1a: Historical abundances of the Kyoto greenhouse gases
- Table AII.1.1b: Historical abundances of the Montreal Protocol greenhouse gas (all ppt)
- Table AII.1.2: Historical effective radiative forcing (ERF) (W m–2), including land use change (LUC)
- Table AII.1.3: Historical global decadal-mean global surface-air temperature (°C) relative to 1961–1990 average
- Table AII.2.1a: Anthropogenic CO2 emissions from fossil fuels and other industrial sources (FF) (PgC yr–1)
- Table AII.2.1b: Anthropogenic CO2 emissions from agriculture, forestry, land use (AFOLU) (PgC yr–1)
- Table AII.2.1c: Anthropogenic total CO2 emissions (PgC yr–1)
- Table AII.2.2: Anthropogenic CH4 emissions (Tg yr–1)
- Table AII.2.3: Anthropogenic N2O emissions (TgN yr–1)
- Table AII.2.4: Anthropogenic SF6 emissions (Gg yr–1)
- Table AII.2.5: Anthropogenic CF4 emissions (Gg yr–1)
- Table AII.2.6: Anthropogenic C2F6 emissions (Gg yr–1)
- Table AII.2.7: Anthropogenic C6F14 emissions (Gg yr–1)
- Table AII.2.8: Anthropogenic HFC-23 emissions (Gg yr–1)
- Table AII.2.9: Anthropogenic HFC-32 emissions (Gg yr–1)
- Table AII.2.10: Anthropogenic HFC-125 emissions (Gg yr–1)
- Table AII.2.11: Anthropogenic HFC-134a emissions (Gg yr–1)
- Table AII.2.12: Anthropogenic HFC-143a emissions (Gg yr–1)
- Table AII.2.13: Anthropogenic HFC-227ea emissions (Gg yr–1)
- Table AII.2.14: Anthropogenic HFC-245fa emissions (Gg yr–1)
- Table AII.2.15: Anthropogenic HFC-43-10mee emissions (Gg yr–1)
- Table AII.2.16: Anthropogenic CO emissions (Tg yr–1)
- Table AII.2.17: Anthropogenic NMVOC emissions (Tg yr–1)
- Table AII.2.18: Anthropogenic NOX emissions (TgN yr–1)
- Table AII.2.19: Anthropogenic NH3 emissions (TgN yr–1)
- Table AII.2.20: Anthropogenic SOX emissions (TgS yr–1)
- Table AII.2.21: Anthropogenic OC aerosols emissions (Tg yr–1)
- Table AII.2.22: Anthropogenic BC aerosols emissions (Tg yr–1)
- Table AII.2.23: Anthropogenic nitrogen fixation (Tg-N yr–1)
- Table AII.3.1a: Net land (natural and land use) CO2 emissions (PgC yr–1)
- Table AII.3.1b: Net ocean CO2 emissions (PgC yr–1)
- Table AII.4.1: CO2 abundance (ppm)
- Table AII.4.2: CH4 abundance (ppb)
- Table AII.4.3: N2O abundance (ppb)
- Table AII.4.4: SF6 abundance (ppt)
- Table AII.4.5: CF4 abundance (ppt)
- Table AII.4.6: C2F6 abundance (ppt)
- Table AII.4.7: C6F14 abundance (ppt)
- Table AII.4.8: HFC-23 abundance (ppt)
- Table AII.4.9: HFC-32 abundance (ppt)
- Table AII.4.10: HFC-125 abundance (ppt)
- Table AII.4.11: HFC-134a abundance (ppt)
- Table AII.4.12: HFC-143a abundance (ppt)
- Table AII.4.13: HFC-227ea abundance (ppt)
- Table AII.4.14: HFC-245fa abundance (ppt)
- Table AII.4.15: HFC-43-10mee abundance (ppt)
- Table AII.4.16: Montreal Protocol greenhouse gas abundances (ppt)
- Table AII.5.1: Stratospheric O3 column changes (DU)
- Table AII.5.2: Tropospheric O3 column changes (DU)
- Table AII.5.3: Total aerosol optical depth (AOD)
- Table AII.5.4: Absorbing aerosol optical depth (AAOD)
- Table AII.5.5: Sulphate aerosol atmospheric burden (TgS)
- Table AII.5.6: OC aerosol atmospheric burden (Tg)
- Table AII.5.7: BC aerosol atmospheric burden (Tg)
- Table AII.5.8: CH4 atmospheric lifetime (yr) against loss by tropospheric OH
- Table AII.5.9: N2O atmospheric lifetime (yr)
- Table AII.6.1: ERF from CO2 (W m–2)
- Table AII.6.2: ERF from CH4 (W m–2)
- Table AII.6.3: ERF from N2O (W m–2)
- Table AII.6.4: ERF from all HFCs (W m–2)
- Table AII.6.5: ERF from all PFCs and SF6 (W m–2)
- Table AII.6.6: ERF from Montreal Protocol greenhouse gases (W m–2)
- Table AII.6.7a: ERF from stratospheric O3 changes since 1850 (W m–2)
- Table AII.6.7b: ERF from tropospheric O3 changes since 1850 (W m–2)
- Table AII.6.8: Total anthropogenic ERF from published RCPs and SRES (W m–2)
- Table AII.6.9: ERF components relative to 1850 (W m–2) derived from ACCMIP
- Table AII.6.10: Total anthropogenic plus natural ERF (W m–2) from CMIP5 and CMIP3, including historical
- Table AII.7.1: Global mean surface O3 change (ppb)
- Table AII.7.2: Surface O3 change (ppb) for HTAP regions
- Table AII.7.3: Surface O3 change (ppb) from CMIP5/ACCMIP for continental regions
- Table AII.7.4: Surface particulate matter change (log10[PM2.5(microgram/m3)]) from CMIP5/ACCMIP for continental regions
- Table AII.7.5: CMIP5 (RCP) and CMIP3 (SRES A1B) global mean surface temperature change (°C) relative to 1986–2005 reference period
- Table AII.7.6: Global mean surface temperature change (°C) relative to 1990 from the TAR
- Table AII.7.7: Global mean sea level rise (m) with respect to 1986–2005 at 1 January on the years indicated

## Method
The data is in in Excel workbook, which contains multiple Excel worksheets. So this is what we do to extract the data:
1. Go to the worksheet of interest.
2. Copy the area (cells) that contain the data.
3. Paste into a new Excel document.
4. Save or export the new file as CSV (Comma-Separated Values) file.
5. Read the file using Python code.
6. Plot the data using Matplotlib.
