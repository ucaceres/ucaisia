var express = require('express') // Llamando a Express
var app = express()               

var port = process.env.PORT || 8080  // Se establece el puerto

app.get('/', function(req, res) {
  res.json({ mensaje: '¡¡¡¡ Hola Mundo Cruel !!!!' })   
})

app.get('/cervezas', function(req, res) {
  res.json({ mensaje: '¡¡¡¡ A beber Cerveza de la wena !!!!' })  
})

app.post('/', function(req, res) {
  res.json({ mensaje: 'Método post' })   
})

app.del('/', function(req, res) {
  res.json({ mensaje: 'Método delete' })  
})

// Se inicia el servidor
app.listen(port)
console.log('API escuchando en el puerto :' + port)
