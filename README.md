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
