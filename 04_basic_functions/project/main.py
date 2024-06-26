def display_menu():
    menu = {
        "1": "1: Add a Book",
        "2": "2: Edit a Book",
        "3": "3: Search for Books",
        "4": "4: Delete a Book",
        "5": "5: View Library Stats",
        "6": "6: Exit App"
    }
    print("=================================================")
    print(" Welcome to your personal books digital library!")
    print("=================================================")
    while True:
        for key in menu:
            print(menu[key])
        user_input = input("\nPlease select from 1 to 6 : ").strip()
        if user_input.isdigit() and user_input in menu:
            return user_input
        else:
            print("\nInvalid input. Please enter a number from 1 to 6.")
        
# [] 空のリストで初期化する
bookshelf = []

# 本を追加する関数
def add_book(bookshelf):
    while True:
        title = input("[Add a book] Enter the title of the book: ").strip()
        if not title:  # タイトルが空の場合はエラー表示して再入力を求める
            print("\nTitle cannot be empty. Please try again.")
            continue  #ループの先頭に戻る
        
        while True: #既読確認で無効な値が入力された場合はエラー表示して再入力を求める
            read_status = input("Did you read it? (yes or no): ").strip()
            if read_status in {"yes", "no"}:
                break
            print("\nInvalid input. Please enter 'yes' or 'no'.")
        
        # 本の ID を割り当てる
        if not bookshelf:
            new_id = 1
        else:
            new_id = bookshelf[-1]['book_id'] + 1
        
        new_book = {
            'book_id': new_id, # IDは自動割り当て
            'title': title,
            'read_status': read_status
        }
        bookshelf.append(new_book) # ブックシェルフに本を追加
        print("New book added successfully.")
        break  # 本の追加が完了したらループを抜ける

    
# 本を編集する関数（既存アイテムの編集）1冊の本を編集
def edit_book(bookshelf):
    while True:
        try:
            book_id = int(input("[Edit a book] Enter the ID of the book to edit: "))
            if book_id < 1:
                print("Invalid input. Please enter a valid ID.")
                continue
        except ValueError:
            print("\nInvalid input. Please enter a valid ID.")
            continue

        found_book = None
        for book in bookshelf:
            if book['book_id'] == book_id:
                found_book = book
                break

        if not found_book:
            print("\nBook not found. Please enter a valid ID.")
            continue

        print("\nBook ID:", found_book['book_id'])
        print("Title:", found_book['title'])
        print("Read Status:", found_book['read_status'])
            
        while True:
            print("\nWhat do you want to edit for this book?")
            print("1. Title")
            print("2. Read status")
            choice = input("Enter your choice (1 or 2): ").strip()
    
            if choice == "1":
                new_title = input("\nEnter the new title: ").strip()
                if new_title:
                    found_book['title'] = new_title
                    print("\nTitle updated successfully.\n")
                    break  # タイトルが更新されたら、編集選択画面に戻る
                else:
                    print("\nInvalid input. Title cannot be empty. Please try again.")
                    continue  # タイトルが空の場合、再度タイトルの入力を求める
            elif choice == "2":
                new_read_status_input = input("Is the book read already? (yes = yes / no = no): ").strip()
                if new_read_status_input in {"yes", "no"}:
                    found_book['read_status'] = new_read_status_input
                    print("\nRead status updated successfully.")
                    break  # 読了ステータスが更新されたら、編集選択画面に戻る
                else:
                    print("\nInvalid input. Please enter 'yes' or 'no'.")
                    continue  # 読了ステータスが無効な場合、再度読了ステータスの入力を求める
            else:
                print("\nInvalid input. please enter '1' or '2'.")
                continue
            break  # 入力値が無効な場合、編集選択画面に戻る
        break



# 本を検索する関数（既存アイテムの検索）検索条件に一致する本（０冊以上）を一覧表示
def search_for_books(bookshelf):
    while True:
        print("\n[Search for books] Choose search option:")
        print("1. Search by title")
        print("2. Search by read status")
        choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if choice == "1":
            while True:
                search_query = input("[Search by title] Enter search keyword: ").strip().lower()
                if search_query:
                    search_results = []
                    for book in bookshelf:
                        if search_query in book['title'].lower():
                            search_results.append(book)
                    if search_results:
                        break  # 検索結果が得られたらループを抜ける
                    else:
                        print("\nNo matching books found. Please try again.")
                else:
                    print("\nInvalid input. Title cannnot be empty.")
            break  # 検索処理が完了したら外側のループを抜ける
          
        elif choice == "2":
            while True:
                search_query = input("[Search by read status] (read = yes / unread = no): ").strip().lower()
                if search_query in {"yes", "no"}:
                    search_results = [book for book in bookshelf if search_query in book['read_status'].lower()]
                    if search_results:
                        break  # 検索結果が得られたらループを抜ける
                    else:
                        print("\nNo matching books found. Please try again.")
                else:
                    print("\nInvalid input for read status. Please enter 'yes' or 'no'.")
            break  # 検索処理が完了したら外側のループを抜ける
        else:
            print("\nInvalid choice. Please enter either '1' or '2'.")
        
    print("\nSearch Results:")
    for result in search_results:
        print(f"ID: {result['book_id']}")
        print(f"Title: {result['title']}")
        print(f"Read Status: {result['read_status']}\n")


# 本を削除する関数（既存アイテムの削除）一冊の本を削除
def delete_book(bookshelf):
    while True:
        try: 
            book_id = int(input("\n [Delete a book] Enter the book ID to delete: "))
            found = False # IDが見つからなかった場合
            for book in bookshelf:
                if book['book_id'] == book_id:
                    # 削除を確認
                    print(f"\nAre you sure to delete this book? \n\nBook ID: {book_id} \nTitle: {book['title']} \nRead Status: {book['read_status']}\n")
                    while True:
                        confirmation = input("\nEnter 'YES' to confirm deletion, 'NO' to cancel: ").strip().lower()
                        if confirmation == "yes":
                            # 本を削除
                            bookshelf.remove(book)
                            print("\nThe book has been deleted successfully.")
                            found = True #yesが入力された場合
                            break
                        elif confirmation == "no":
                            print("\n[Delete a book] is canceled.")
                            found = True #noが入力された場合
                            break
                        else:
                            print("\nInvalid input. Please enter 'yes' or 'no'.")
                            continue # ループを中断してyes or no の入力を促す
                    break
            if not found:
                print("\nInvalid book ID. Please enter a valid book ID.")
            break
        except ValueError:
            print("\nInvalid input. Book ID has to be a number.")


# ブックシェルフの統計情報を表示する関数：ブックシェルフ内の本の総数、既読の本の数、未読の本の数を表示
def count_read(bookshelf): #既読の本を合計する関数
    read_books_total = sum(1 for book in bookshelf if book['read_status'] == "yes")
    return read_books_total

def count_unread(bookshelf): #未読の本を合計する関数
    unread_books_total = sum(1 for book in bookshelf if book['read_status'] == "no")
    return unread_books_total

def view_library_stats(bookshelf): #統計を表示する
        total_books = len(bookshelf) #登録されている本の総数
        read_books_total = count_read(bookshelf) 
        unread_books_total = count_unread(bookshelf)  
        print("\n[Library Stats]")
        print(f"Total number of books: {total_books}")
        print(f"Number of read books: {read_books_total}")
        print(f"Number of unread books: {unread_books_total}\n")
 
# アプリケーションを終了する関数を定義
def exit_app():
    print("\n[Exit app] Exiting the application.\n")
    exit()

# メニュー画面を表示し、ユーザーの入力を受け取る
def main():
    bookshelf = []
    while True:
        user_input = display_menu() 
        if user_input == "1":
            add_book(bookshelf)
        elif user_input == "2":
            edit_book(bookshelf)
        elif user_input == "3":
            search_for_books(bookshelf)
        elif user_input == "4":
            delete_book(bookshelf)
        elif user_input == "5":
            view_library_stats(bookshelf)
        else:
            exit_app()
        
if __name__ == "__main__":
    main()
