import express from "express";
import http from "http";
import { WebSocketServer, WebSocket as IWebsocket } from "ws";

import apiRouter from "./api/routes/index.router";

const app = express();
export const server = http.createServer(app);
export const websocket = new WebSocketServer({ server });

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use("/api", apiRouter);

function send5Time({
  socket,
  message,
  interval,
  numberOfTimes,
}: {
  socket: IWebsocket;
  message: string;
  interval: number;
  numberOfTimes: number;
}) {
  const Interval = setInterval(() => {
    socket.send(message);
    if (numberOfTimes === 0) clearInterval(Interval);
    numberOfTimes -= 1;
  }, interval * 1000);
}

websocket.on("connection", (socket) => {
  console.log("User connected");
  socket.send("sucessfully connected to socket");

  send5Time({ socket, message: "hello", interval: 3, numberOfTimes: 10 });

  socket.on("message", (message) => {
    console.log(message.toString());
  });

  socket.on("disconnect", () => {
    console.log("user disconnected!");
    socket.send("disconnected");
  });
});

export default app;
