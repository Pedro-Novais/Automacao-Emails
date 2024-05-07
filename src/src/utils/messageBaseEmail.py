def get_message_base_html(lines):

    msg = """
    <html>
        <head></head>
        <body>
            <p>Boa tarde.</p>

            <p>Prezados,</p>

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

            

            <p style='background-color:#ffff00'> Em caso de atraso: </p>
            <p> 
                5.6.1. O atraso em qualquer dos pagamentos devidos em período superior a 30 (trinta) dias ensejará um ou mais dos seguintes efeitos, cumulativamente e conforme aplicável: (i) em relação aos Serviços: a imediata suspensão da prestação dos Serviços até que todos os débitos tenham sido integralmente pagos, 
                considerando-se o valor principal acrescido dos encargos moratórios da Cláusula 5.6 acima; (ii) em relação à Licença do Software: imediata suspensão da Licença do Software e da prestação dos Serviços, até que todos os débitos tenham sido integralmente pagos, considerando-se o valor principal acrescido dos encargos moratórios da Cláusula 5.6 acima.
                5.6.2. Decorridos 60 (sessenta) dias da emissão da cobrança da Licença do Software, sem o devido pagamento, a utilização do Software será imediatamente interrompida de forma definitiva, sem necessidade de notificação da E-DEPLOY à Licenciada.
            </p>

            <p>Qualquer dúvida estou à disposição,</p>

            <p>Att,.</p>
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