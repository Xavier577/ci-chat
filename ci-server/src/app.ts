import express from "express";
import http from "http";
import { WebSocketServer } from "ws";

import apiRouter from "./api/routes/index.router";

const app = express();
export const server = http.createServer(app);
export const websocket = new WebSocketServer({ server });

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get("/", (_req, res) => {
  res.send(`<script>
  const ws = new WebSocket("")
  
  ws.on
  </script>`);
});
app.use("/api", apiRouter);

websocket.on("connection", (socket) => {
  console.log("User connected");
  socket.send("sucessfully connected to socket");

  socket.on("message", (message) => {
    console.log(message.toString());
  });

  socket.on("disconnect", () => {
    console.log("user disconnected!");
    socket.send("disconnected");
  });
});

export default app;
