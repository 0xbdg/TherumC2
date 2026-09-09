from therum import Therum, socket

app = Therum()

if __name__ == "__main__":
    #app.run()
    socket.run(app,debug=True)
