from string import Template


class PurchaseSummaryTemplate:
    def __init__(self):
        self.template = Template("""
        <!DOCTYPE html>
        <html>
        <head>
          <meta charset="UTF-8" />
          <title>Resumen de Compra</title>
          <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f4; color: #333; padding: 20px; }
            .container { background-color: #fff; padding: 20px; border-radius: 8px; max-width: 600px; margin: auto; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); }
            h2 { color: #007BFF; }
            .info { margin-bottom: 10px; }
            .label { font-weight: bold; }
            .body-text { margin-top: 20px; white-space: pre-wrap; }
          </style>
        </head>
        <body>
          <div class="container">
            <h2>Resumen del pago</h2>
            <h3>$body</h3>
            <div class="body-text"></div>
          </div>
        </body>
        </html>
        """)

    def render(self, **kwargs) -> str:
        return self.template.substitute(**kwargs)
