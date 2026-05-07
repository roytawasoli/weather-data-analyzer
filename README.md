# 🌦️ Weather Data Analyzer

A lightweight Python tool to analyze weather data from a CSV file.  
Detects missing sensor readings, calculates statistics, flags strong winds, finds the coldest records, and converts temperatures to Fahrenheit.

---

## ✨ Features

- 🔍 **Broken sensor detection** – Identifies missing values in temperature, rainfall, or wind speed columns.
- 📊 **Temperature & wind statistics** – Shows the highest recorded temperature and the average wind speed.
- ⚠️ **Strong wind warning** – Lists all records where wind speed exceeds 20 km/h.
- ❄️ **Three coldest records** – Sorts data from lowest to highest temperature and displays the top 3.
- 🌡️ **Fahrenheit conversion** – Adds a new column with temperatures in Fahrenheit and previews the first 5 rows.

---

## 📁 CSV File Format

The input file must be named `weather_data.csv` and placed in the same folder as the script.

```csv
Date,City,Temperature_C,Rainfall_mm,WindSpeed_kmh
2026-04-01,Tehran,18.5,0.0,15
2026-04-02,Tabriz,12.0,5.2,22
2026-04-03,Ahvaz,8.5,12.0,30
2026-04-04,Tehran,20.1,0.0,10
2026-04-05,Shiraz,32.0,0.0,8
2026-04-06,Tabriz,10.5,8.5,25
2026-04-07,Ahvaz,15.0,,18
2026-04-08,Shiraz,35.2,0.0,12
```
- Note: Empty cells (two commas in a row) represent missing sensor readings.

---

## 🚀 How to Run

  - 1. Ensure you have Python 3 installed.

  - 2. Save the script as weather_analyzer.py and place weather_data.csv in the same directory.

  - 3. Open a terminal in that folder and run:

    ```bash
    python weather_analyzer.py
    ```
  - 4. Use the interactive menu:

    ```text
    ========================================
    Menu:
    1 - Check broken sensors (Part 2)
    2 - Max temp & average wind (Part 3)
    3 - Strong wind warning (Part 4)
    4 - Three coldest records (Part 5)
    5 - Add Fahrenheit & show first 5 rows (Part 6)
    0 - Exit
    Please enter a number:
    ```

---

## 📸 Example Output

  - Option 1 – Broken sensors

  ```text
  --- Part 2: Broken sensors (missing data) ---
  ⚠️ On 2026-04-07 in Ahvaz: rain_gauge recorded no value.
      → Rain gauge is broken.
  ```

  - Option 4 – Three coldest records

  ```text
  --- Part 5: Three coldest records ---
  2026-04-03,Ahvaz,8.5,12.0,30
  2026-04-06,Tabriz,10.5,8.5,25
  2026-04-02,Tabriz,12.0,5.2,22
  ```

  - Option 5 – Fahrenheit conversion

  ```text
  --- Part 6: Add Fahrenheit column & first 5 rows ---
  Date,City,Temperature_C,Rainfall_mm,WindSpeed_kmh,Temperature_F
  2026-04-01,Tehran,18.5,0.0,15,65.3
  2026-04-02,Tabriz,12.0,5.2,22,53.6
  2026-04-03,Ahvaz,8.5,12.0,30,47.3
  2026-04-04,Tehran,20.1,0.0,10,68.2
  2026-04-05,Shiraz,32.0,0.0,8,89.6
  ```

---

## 📦 Requirements

  - Python 3.x (no external libraries – only built‑in modules)

---

## 📝 Code Structure

   - nested_data – 2D list storing all rows from the CSV.
   - part2_check_broken_sensors() – Detects empty cells in temperature, rainfall, or wind.
   - part3_max_temp_avg_wind() – Calculates highest temperature and average wind speed.
   - part4_wind_warning() – Filters and displays rows with wind > 20 km/h.
   - part5_coldest_three() – Sorts rows by temperature and shows the three lowest.
   - part6_add_fahrenheit() – Adds a Fahrenheit column and prints the first 5 rows.

---

## 🤝 Contributing

   Issues and pull requests are welcome. Feel free to improve the code or documentation.

---

## 📄 License

   This project is licensed under the MIT License – see the [LICENSE](https://duckduckgo.com/) file for details.

---

### Author: Roy
### GitHub: [roytawasoli](https://github.com/roytawasoli/)

---

# 🌦️ تحلیل‌گر داده‌های هواشناسی

یک ابزار پایتونی سبک برای تحلیل داده‌های هواشناسی از فایل CSV.
این ابزار داده‌های خالی سنسورها را تشخیص می‌دهد، آمار دما و باد را محاسبه می‌کند، رکوردهای دارای باد شدید را نشان می‌دهد، سه روز سردترین را پیدا می‌کند و دما را به فارنهایت تبدیل می‌نماید.

---

## ✨ قابلیت‌ها

- 🔍 تشخیص سنسور خراب – مقادیر خالی دما، بارش یا سرعت باد را شناسایی می‌کند.
- 📊 آمار دما و باد – بالاترین دمای ثبت شده و میانگین سرعت باد را نشان می‌دهد.
- ⚠️ هشدار باد شدید – تمام رکوردهایی که سرعت باد بیشتر از ۲۰ کیلومتر بر ساعت دارند را لیست می‌کند.
- ❄️ سه رکورد سردترین – داده‌ها را از سردترین به گرم‌ترین مرتب کرده و سه تای اول را نمایش می‌دهد.
- 🌡️ تبدیل به فارنهایت – ستون جدیدی با دمای فارنهایت اضافه کرده و ۵ سطر اول را نشان می‌دهد.

---

## 📁 فرمت فایل CSV

فایل ورودی باید `weather_data.csv` نام داشته باشد و در کنار برنامه قرار گیرد.

```csv
Date,City,Temperature_C,Rainfall_mm,WindSpeed_kmh
2026-04-01,Tehran,18.5,0.0,15
2026-04-02,Tabriz,12.0,5.2,22
2026-04-03,Ahvaz,8.5,12.0,30
2026-04-04,Tehran,20.1,0.0,10
2026-04-05,Shiraz,32.0,0.0,8
2026-04-06,Tabriz,10.5,8.5,25
2026-04-07,Ahvaz,15.0,,18
2026-04-08,Shiraz,35.2,0.0,12
```
- نکته: خانه‌های خالی (دو ویرگول پشت سر هم) به معنی ثبت نشدن داده از آن سنسور است.

---

## 🚀 نحوه اجرا

  - 1. اطمینان حاصل کنید که Python 3 نصب است.

  - 2. اسکریپت را با نام weather_analyzer.py ذخیره کرده و فایل weather_data.csv را در همان پوشه قرار دهید.

  - 3. ترمینال را در آن پوشه باز کرده و اجرا کنید:

    ```bash
    python weather_analyzer.py
    ```
  - 4. از منوی تعاملی استفاده کنید:

    ```text
    ========================================
    Menu:
    1 - Check broken sensors (Part 2)
    2 - Max temp & average wind (Part 3)
    3 - Strong wind warning (Part 4)
    4 - Three coldest records (Part 5)
    5 - Add Fahrenheit & show first 5 rows (Part 6)
    0 - Exit
    Please enter a number:
    ```

---

## 📸 خروجی نمونه

  - گزینه ۱ – سنسورهای خراب

  ```text
  --- Part 2: Broken sensors (missing data) ---
  ⚠️ On 2026-04-07 in Ahvaz: rain_gauge recorded no value.
      → Rain gauge is broken.
  ```

  - گزینه ۴ – سه رکورد سردترین

  ```text
  --- Part 5: Three coldest records ---
  2026-04-03,Ahvaz,8.5,12.0,30
  2026-04-06,Tabriz,10.5,8.5,25
  2026-04-02,Tabriz,12.0,5.2,22
  ```

  - گزینه ۵ – تبدیل به فارنهایت

  ```text
  --- Part 6: Add Fahrenheit column & first 5 rows ---
  Date,City,Temperature_C,Rainfall_mm,WindSpeed_kmh,Temperature_F
  2026-04-01,Tehran,18.5,0.0,15,65.3
  2026-04-02,Tabriz,12.0,5.2,22,53.6
  2026-04-03,Ahvaz,8.5,12.0,30,47.3
  2026-04-04,Tehran,20.1,0.0,10,68.2
  2026-04-05,Shiraz,32.0,0.0,8,89.6
  ```

---

## 📦 نیازمندی‌ها

  - Python 3.x (بدون نیاز به کتابخانه‌های اضافی – فقط ماژول‌های داخلی)

---

## 📝 ساختار کد

   - nested_data – لیست دو بعدی حاوی تمام سطرهای CSV.
   - is_empty() / to_float() – توابع کمکی برای مدیریت داده‌های خالی.
   - part2_check_broken_sensors() – شناسایی خانه‌های خالی دما، بارش یا باد.
   - part3_max_temp_avg_wind() – محاسبه بیشترین دما و میانگین سرعت باد.
   - part4_wind_warning() – فیلتر و نمایش ردیف‌هایی با سرعت باد بیش از ۲۰.
   - part5_coldest_three() – مرتب‌سازی بر اساس دما و نمایش سه رکورد سردترین.
   - part6_add_fahrenheit() – افزودن ستون فارنهایت و چاپ ۵ سطر اول.

---

## 🤝 مشارکت

   پیشنهادات و درخواست‌های `pull request` پذیرفته می‌شود. خوشحال می‌شویم کد یا مستندات را بهبود دهید.

---

### نویسنده : Roy
### گیت هاب : [roytawasoli](https://github.com/roytawasoli/)

---
