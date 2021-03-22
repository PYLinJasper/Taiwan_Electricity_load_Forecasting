# Taiwan_Electricity_load_Forecasting
Using data mining and ML technique

# 資料分析
- 電力需求與天氣息息相關，台灣大多數人口聚集於台北、新北與高雄市，因此決定搜集此三座城市的最高與最低溫。
- 將備轉容量與地區氣溫做圖後，發現新北與高雄的氣溫波形與備轉容量較相似
  - 台北![截圖 2021-03-22 下午11 50 17](https://user-images.githubusercontent.com/48174852/112018956-f8630d00-8b69-11eb-9970-52bc9c5d1807.png)
  - 新北![截圖 2021-03-22 下午11 50 12](https://user-images.githubusercontent.com/48174852/112018643-ba65e900-8b69-11eb-8f90-7b6b4581d204.png)
  - 高雄![截圖 2021-03-22 下午11 50 12拷貝](https://user-images.githubusercontent.com/48174852/112019052-0b75dd00-8b6a-11eb-8632-46cbe66a3ca1.png)
- 將備轉容量與高溫低溫做圖後，發現與最低氣溫最有關聯
  - 高溫![截圖 2021-03-22 下午11 50 12拷貝2](https://user-images.githubusercontent.com/48174852/112019340-509a0f00-8b6a-11eb-892b-4d92a1476570.png)
  - 低溫![截圖 2021-03-22 下午11 50 17拷貝](https://user-images.githubusercontent.com/48174852/112019336-4e37b500-8b6a-11eb-9dcc-d2ad1367465f.png)
## 資料分析小結
- 綜合上幾張圖片可發現備轉容量與2020年以後的波形較為吻合所以採用2020以後之資料
- 觀察後發現最低溫與預測較有關聯，但為增加資料量採用三個城市之最高、最低溫
