import sqlite3

class AsiaTeachersPipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect("teachers.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS teachers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                expertise TEXT
            )
        ''')
        self.conn.commit()

    def process_item(self, item, spider):
        self.cursor.execute('''
            INSERT INTO teachers (name, expertise) VALUES (?, ?)
        ''', (item['name'], item['expertise']))
        self.conn.commit()
        with open("teachers.txt", "a", encoding="utf-8") as f:
            line = f"{item['name']} 老師: 專長: {item['expertise']}\n"
            f.write(line)
        return item

    def close_spider(self, spider):
        self.conn.close()