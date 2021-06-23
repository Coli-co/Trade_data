from website import create_app

app = create_app()

if __name__ == '__main__':  # 執行目前檔案，而不是import的檔案
    app.run(debug=True)  # 一旦code更改， web server 便會自動重啟
