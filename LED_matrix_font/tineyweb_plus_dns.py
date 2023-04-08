import uasyncio
import tinyweb
import captivedns


# Create web server application
app = tinyweb.webserver()

# create DNS server
#dns = tinydns.Server(domains={'gazotron.com': '192.168.4.1'}, ttl=33)

# Index page
@app.route('/')
async def index(request, response):
    # Start HTTP response with content-type text/html
    await response.start_html()
    # Send actual HTML page
    await response.send(
        """
        <html data-theme="dark" lang='fr'>
            <head>
            <meta charset="utf-8">
            <link rel="stylesheet" href="css/pico.min.css">
            </head>
            <body>
                <main class="container">
                    <hgroup>
                      <h1>Horloge Nixie "Gazotron"</h1>
                      <h3>Un artefact issu de la guerre froide vous donne l'heure...</h3>
                    </hgroup>
                    <hr>
                    <p><code>version 0.1 du 18/12/2022</code></p>
                    <form method="post">
                        <hgroup>
                          <h2>Accès Wifi</h2>
                          <h3>blablabla</h3>
                        </hgroup>
                          <div class="grid">
                            <div><input type="text" name="SSID" placeholder="Point d'accès Wifi (SSID)" aria-label="Point d'accès Wifi (SSID)" required></div>
                          </div>
                          <div class="grid">
                            <input type="text" name="password" placeholder="Mot de passe Wifi" aria-label="Mot de passe Wifi" required>
                          </div>
                          <hgroup>
                            <h2>Réglages</h2>
                            <h3>blablabla</h3>
                          </hgroup>
                          
                              <legend><strong>Switches</strong></legend>
                              <label for="switch-1">
                                <input type="checkbox" id="switch-1" name="switch-1" role="switch" checked="">
                                Switch
                              </label>
                              <label for="switch-2">
                                <input type="checkbox" id="switch-2" name="switch-2" role="switch">
                                Switch
                              </label>
                          
                          <div class="grid">
                            <button type="submit">Sauvegarder</button>
                          </div>
                    </form>
                </main>
                <footer class="container">
                    <hr>
                    <blockquote>"L'heure me regarde et je regarde l'heure."
                        <footer>- Koan zen.</footer>
                    </blockquote>
                </footer>
            </body>
        </html>
        """)

@app.route('/css/pico.min.css')
async def index(req, resp):
    await resp.send_file('pico.min.css.gz', content_encoding='gzip')

# HTTP redirection
@app.route('/redirect')
async def redirect(request, response):
    # Start HTTP response with content-type text/html
    await response.redirect('/')


# Another one, more complicated page
@app.route('/table')
async def table(request, response):
    # Start HTTP response with content-type text/html
    await response.start_html()
    await response.send('<html><body><h1>Simple table</h1>'
                        '<table border=1 width=400>'
                        '<tr><td>Name</td><td>Some Value</td></tr>')
    for i in range(10):
        await response.send('<tr><td>Name{}</td><td>Value{}</td></tr>'.format(i, i))
    await response.send('</table>'
                        '</html>')

def sub_task():
    while True:
        #utime.sleep_ms(500)
        await uasyncio.sleep_ms(250)
        print("ok?")

if __name__ == '__main__':
    loop = uasyncio.get_event_loop()
    #loop.create_task(sub_task())
    loop.create_task(captivedns.run_dns_server())
    # this one runs loop_forever()
    app.run(host='0.0.0.0', port=80)
