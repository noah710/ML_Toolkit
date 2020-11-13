var http = require('http')
var url = require('url')
var fs = require('fs')
var path = require('path')
var net = require('net')

var baseDirectory = __dirname

var port = 8080
var ip_end_base = 10

http.createServer(function (request, response) {
    try {
        if (request.method === 'POST') {
            let body = ''
            request.on('data', chunk => {
                body += chunk.toString() // convert Buffer to string
            })
            request.on('end', () => {
                let ip_end = body.split("=")[1]
                console.log(ip_end)
                let ip_base = '172.32.0.' + (ip_end_base + parseInt(ip_end)).toString()
                let run_port = 8888
                let socket = net.createConnection(run_port, ip_base, () => {
                    console.log("Running app!")
                    socket.write('run\n', () => {
                        socket.destroy()
                    })
                })
                response.writeHead(301,
                    {Location: 'http://localhost:/main.html'}
                  )
                response.end()
            })
        }else{

            var requestUrl = url.parse(request.url)

            // need to use path.normalize so people can't access directories underneath baseDirectory
            var fsPath = baseDirectory+path.normalize(requestUrl.pathname)

            var fileStream = fs.createReadStream(fsPath)
            fileStream.pipe(response)
            fileStream.on('open', function() {
                response.writeHead(200)
            })
            fileStream.on('error',function(e) {
                response.writeHead(404)     // assume the file doesn't exist
                response.end()
            })
        }
   } catch(e) {
        response.writeHead(500)
        response.end()     // end the response so browsers don't hang
        console.log(e.stack)
   }
}).listen(port)

