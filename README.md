--- Chess Ranger 
The rules are simple.
- Pieces move as standard chess pieces.
- You can perform only capture moves.
- You are allowed to capture the king.
- The goal is to end up with one single piece on the board.


---
1. pieces.py: Chứa các lớp quân cờ (Piece, King, Queen, v.v.).
2. game.py: Chứa lớp ChessGame, quản lý trò chơi, điều khiển các lượt đi và kết quả trò chơi.
3. board.py: Chứa lớp Board, quản lý bàn cờ và các thao tác liên quan đến bàn cờ.
4. main.py: - Đây là file chính để chạy trò chơi, nơi sẽ khởi tạo tất cả các đối tượng từ các file khác và điều khiển dòng chảy của trò chơi.
            - Bạn sẽ gọi các hàm từ `board.py` để tạo bàn cờ, sử dụng `pieces.py` để tạo quân, và dùng `game.py` để bắt đầu và điều khiển các bước chơi.


--- 
Hướng đi cụ thể
Bước 1: Xây dựng bàn cờ, vị trí quân cờ ban đầu và trạng thái đích.
Bước 2: Viết hàm trạng thái kế tiếp để tạo danh sách các nước đi hợp lệ.
Bước 3: Hiện thực giải thuật DFS/BrFS.
Bước 4: Hiện thực giải thuật A* hoặc Hill Climbing.
Bước 5: Tạo bảng so sánh thời gian và bộ nhớ tiêu tốn giữa hai giải thuật với các bài toán khác nhau.
Bước 6: Viết báo cáo và tạo video minh họa.

---
self.chess_board trong ChessGame là một đối tượng của lớp Board, dùng để quản lý bàn cờ.
self.board trong Board là một mảng 2D, chứa các quân cờ hoặc None (trống).