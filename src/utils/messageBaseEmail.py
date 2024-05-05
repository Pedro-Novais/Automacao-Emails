def get_message_base_html(lines):

    msg = """
    <html>
        <head></head>
        <body>
            <p>Boa tarde.</p>

            <p>Prezados,</p>

            <p>Como conversado via Whatzapp , segue em anexo os boletos com as datas atualizadas, das renegociações a seguir,</p>

            <table style='font-family: Open Sans, sans-serif;min-height: 3rem;border-spacing: 0;'>

                <tr style='background-color:#8d8d8d;'>

                    <th style='padding: 0.2rem; background-color:#b9b9b9; border-left:solid 1px; border-right:solid 1px; border-bottom:solid 1px; border-top:solid 1px;'>Id Interno</th>
                    <th style='padding: 0.2rem; border-right:solid 1px; border-bottom:solid 1px; border-top:solid 1px;'>Nº Boleto</th>
                    <th style='padding: 0.2rem; background-color:#b9b9b9; border-right:solid 1px; border-bottom:solid 1px; border-top:solid 1px;'>Data de Emissão</th>
                    <th style='padding: 0.2rem; border-right:solid 1px; border-bottom:solid 1px; border-top:solid 1px;'>Nº Nota Fiscal</th>
                    <th style='padding: 0.2rem; background-color:#b9b9b9; border-right:solid 1px; border-bottom:solid 1px; border-top:solid 1px;'>Razão Social</th>
                    <th style='padding: 0.2rem; border-right:solid 1px; border-bottom:solid 1px; border-top:solid 1px;'>CNPJ</th>
                    <th style='padding: 0.2rem; background-color:#b9b9b9; border-right:solid 1px; border-bottom:solid 1px; border-top:solid 1px;'>Descrição do Serviço</th>
                    <th style='padding: 0.2rem; border-right:solid 1px; border-bottom:solid 1px; border-top:solid 1px;'>Valor Bruto</th>
                    <th style='padding: 0.2rem; background-color:#b9b9b9; border-right:solid 1px; border-bottom:solid 1px; border-top:solid 1px;'>Valor Líquido</th>
                    <th style='padding: 0.2rem; border-right:solid 1px; border-bottom:solid 1px; border-top:solid 1px;'>Data de Vencimento</th>

                </tr>
                {}
            </table>

            <p>Qualquer dúvida estou à disposição,</p>

            <p>Att.,</p>
        </body>
    </html>
    """.format(lines)

    return msg

def get_line_html(
        id_interno,
        number_blt,
        date_emission,
        note_fiscal,
        reason_social,
        cnpj,
        description_service,
        value_bruto,
        value_liquid,
        date_vencimento
                  ):

    line = """
            <tr>
                <th style='padding: 0.2rem; background-color:#fff; border-left:solid 1px; border-right:solid 1px; border-bottom:solid 1px; font-size: 0.9rem'>{}</th>
                <th style='padding: 0.2rem; background-color:#fff; border-right:solid 1px; border-bottom:solid 1px; font-size: 0.9rem'>{}</th>
                <th style='padding: 0.2rem; background-color:#fff; border-right:solid 1px; border-bottom:solid 1px; font-size: 0.9rem'>{}</th>
                <th style='padding: 0.2rem; background-color:#fff; border-right:solid 1px; border-bottom:solid 1px; font-size: 0.9rem'>{}</th>
                <th style='padding: 0.2rem; background-color:#fff; border-right:solid 1px; border-bottom:solid 1px; font-size: 0.9rem'>{}</th>
                <th style='padding: 0.2rem; background-color:#fff; border-right:solid 1px; border-bottom:solid 1px; font-size: 1rem; min-width: 10vw'>{}</th>
                <th style='padding: 0.2rem; background-color:#fff; border-right:solid 1px; border-bottom:solid 1px; font-size: 0.9rem'>{}</th>
                <th style='padding: 0.2rem; background-color:#fff; border-right:solid 1px; border-bottom:solid 1px; font-size: 0.9rem'>{}</th>
                <th style='padding: 0.2rem; background-color:#fff; border-right:solid 1px; border-bottom:solid 1px; font-size: 0.9rem'>{}</th>
                <th style='padding: 0.2rem; background-color:#fff; border-right:solid 1px; border-bottom:solid 1px; font-size: 0.9rem'>{}</th>
            </tr> 

            """.format( 
                id_interno,
                number_blt,
                date_emission,
                note_fiscal,
                reason_social,
                cnpj,
                description_service,
                value_bruto,
                value_liquid,
                date_vencimento
                )
    
    return line

# omg = ['teste','teste','teste','teste','teste', 'teste', 'teste','teste','teste', 'teste']

# teste = get_line_html(omg)

# teste2 = get_line_html(omg)

# strd = '{}'.format(teste+teste2)

# aoba = get_message_base_html(strd)

# print(aoba)