# Taiwan_Electricity_load_Forecasting
Using data mining and ML technique

# 資料分析與特徵採用
- 電力需求與天氣息息相關，台灣大多數人口聚集於台北、新北與高雄市，因此決定搜集此三座城市的最高與最低溫。
- 將備轉容量與地區氣溫做圖後，==發現新北與高雄的氣溫波形與備轉容量較相似==
  - 台北![截圖 2021-03-22 下午11 50 17](https://user-images.githubusercontent.com/48174852/112018956-f8630d00-8b69-11eb-9970-52bc9c5d1807.png)
  - 新北![截圖 2021-03-22 下午11 50 12](https://user-images.githubusercontent.com/48174852/112018643-ba65e900-8b69-11eb-8f90-7b6b4581d204.png)
  - 高雄![截圖 2021-03-22 下午11 50 12拷貝](https://user-images.githubusercontent.com/48174852/112019052-0b75dd00-8b6a-11eb-8632-46cbe66a3ca1.png)
- 將備轉容量與高溫低溫做圖後，發現==與最低氣溫最有關聯==
  - 高溫![截圖 2021-03-22 下午11 50 12拷貝2](https://user-images.githubusercontent.com/48174852/112019340-509a0f00-8b6a-11eb-892b-4d92a1476570.png)
  - 低溫![截圖 2021-03-22 下午11 50 17拷貝](https://user-images.githubusercontent.com/48174852/112019336-4e37b500-8b6a-11eb-9dcc-d2ad1367465f.png)
## 資料分析與特徵採用小結
- 綜合上幾張圖片可發現備轉容量與2020年以後的波形較為吻合所以==採用2020以後之資料==
- 觀察後發現最低溫與預測較有關聯，但為增加資料量==採用三個城市之最高、最低溫==
- 同時也採用==前一天的備轉容量==當作輸入

# 資料前處理與模型訓練
- 因為此預測為==時序性資料預測故採用LSTM(Long Short Term Memory)來進行模型訓練==。
  - LSTM示意圖![圖片 1](https://user-images.githubusercontent.com/48174852/112021841-aa9bd400-8b6c-11eb-81a0-5c60883cefeb.png)
- 我們訓練共採用前面所提到的==三個城市之最高、最低溫與前一天的備轉容量共7個特徵值，將七個特徵值包成一天，再將七天包成一個輸入值==
- 將輸入值丟入模型訓練後，我們預期模型能==輸出一整個禮拜的預估數值==
  - 示意圖![截圖 2021-03-23 上午12 13 30](https://user-images.githubusercontent.com/48174852/112022291-2138d180-8b6d-11eb-9444-785d65d08deb.png)


