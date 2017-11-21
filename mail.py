from sparkpost import SparkPost

sp = SparkPost('2a5e51536720e107050b8ec31e7428cea9266ca4')

response = sp.transmissions.send(
    use_sandbox=True,
    recipients=['prateekkumar1612@gmail.com'],
    html='<p>Intruder Alert</p>',
    from_email='test@sparkpostbox.com',
    subject='Smart System'
)

print(response)
