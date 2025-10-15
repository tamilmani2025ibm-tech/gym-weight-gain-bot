document.getElementById("chat-form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const msgInput = document.getElementById("message");
  const chatBox = document.getElementById("chat-box");
  const message = msgInput.value;

  chatBox.innerHTML += `<div class="user">You: ${message}</div>`;

  const formData = new FormData();
  formData.append("message", message);

  const response = await fetch("/chat", { method: "POST", body: formData });
  const data = await response.json();

  chatBox.innerHTML += `<div class="bot">Bot: ${data.reply}</div>`;
  msgInput.value = "";
  chatBox.scrollTop = chatBox.scrollHeight;
});
