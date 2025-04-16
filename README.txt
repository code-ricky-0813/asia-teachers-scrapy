【作業說明】
讀取每個老師的專長／Discipline expertise
存成一個文字檔，可以是txt, csv或json格式

【執行方式】
進入 asia_teachers 專案資料夾，於終端機輸入：

    scrapy crawl teachers

執行完後，會在專案資料夾下產生：
- teachers.db  → SQLite 資料庫檔案，儲存老師姓名與專長
- teachers.txt → 純文字檔，每行格式為：
                  姓名 老師: 專長: 專長內容