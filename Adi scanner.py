#বোকাচোদা script দেখস কেন 🖕


import base64

# Base64 encoded content
encoded_content = '''aW1wb3J0IHN1YnByb2Nlc3MKaW1wb3J0IHN5cwppbXBvcnQgdGltZQppbXBvcnQgb3MKCmRlZiBjbGVhcigpOgogICAgb3Muc3lzdGVtKCdjbGVhcicpCgpkZWYgcHJpbnRfYXNjaWlfYXJ0KCk6CiAgICAjIEFOU0kgZXNjYXBlIGNvZGVzIGZvciBjb2xvcnMKICAgIEdSRUVOID0gJ1wwMzNbOTJtJwogICAgUkVTRVQgPSAnXDAzM1swbScKCiAgICBhc2NpaV9hcnQgPSBmIiIiCntHUkVFTn0KCiAgICAgICAgICAgICBfX18gICAgX19fXyAgX19fX19fX18gIF9fX19fX19fX19fX19fXwogICAgICAgICAgICAvICAgfCAgLyBfXyBcLyAgXy8gX18gXC9fICBfXy9fICBfXy8gICB8ICAgICAgIGNvZGUgYnkgYWRpcnR0YSDwn5iOCiAgICAgICAgICAgLyAvfCB8IC8gLyAvIC8vIC8vIC9fLyAvIC8gLyAgIC8gLyAvIC98IHwgICAgICAgVEhBTksgWU9VIEZPUiBVU0UgTVkgVE9PTOKdpAogICAgICAgICAgLyBfX18gfC8gL18vIC8vIC8vIF8sIF8vIC8gLyAgIC8gLyAvIF9fXyB8ICAgICAgIGRvbid0IGNvcHkgbXkgdG9vbCDwn6SXCiAgICAgICAgIC9fLyAgfF8vX19fX18vX19fL18vIHxffCAvXy8gICAvXy8gL18vICB8X3wgICAgIG15IGdpdGh1YiBpZDogKGdpdGh1Yi5jb20vQURJUlRUQSkKCntSRVNFVH0KIiIiCiAgICBwcmludChhc2NpaV9hcnQpCgpkZWYgc2Nhbl9uZXR3b3JrKHRhcmdldCk6CiAgICAjIEFOU0kgZXNjYXBlIGNvZGVzIGZvciBjb2xvcnMKICAgIEdSRUVOID0gJ1wwMzNbOTJtJwogICAgUkVEID0gJ1wwMzNbOTFtJwogICAgUkVTRVQgPSAnXDAzM1swbScKCiAgICAjIFJ1bm5pbmcgbm1hcCBhcyBhIHN1YnByb2Nlc3MgYW5kIGNhcHR1cmluZyB0aGUgb3V0cHV0CiAgICB0cnk6CiAgICAgICAgcHJpbnQoZiJ7R1JFRU59U2Nhbm5pbmcuLi57UkVTRVR9IikKICAgICAgICAjIFN0YXJ0IHRpbWUgZm9yIHBlcmZvcm1hbmNlIG1lYXN1cmVtZW50CiAgICAgICAgc3RhcnRfdGltZSA9IHRpbWUudGltZSgpCgogICAgICAgICMgVXNpbmcgbm1hcCB3aXRoIG9wdGltaXphdGlvbnMKICAgICAgICAjIC1UNDogVGltaW5nIHRlbXBsYXRlIHRvIHNwZWVkIHVwIHNjYW5uaW5nCiAgICAgICAgIyAtcDEtMTAwMDogU2NhbiB0aGUgbW9zdCBjb21tb24gMTAwMCBwb3J0cwogICAgICAgIHJlc3VsdCA9IHN1YnByb2Nlc3MucnVuKFsnbm1hcCcsICctVDQnLCAnLXAxLTEwMDAnLCB0YXJnZXRdLCBzdGRvdXQ9c3VicHJvY2Vzcy5QSVBFLCBzdGRlcnI9c3VicHJvY2Vzcy5QSVBFLCB0ZXh0PVRydWUpCgogICAgICAgICMgRW5kIHRpbWUgZm9yIHBlcmZvcm1hbmNlIG1lYXN1cmVtZW50CiAgICAgICAgZW5kX3RpbWUgPSB0aW1lLnRpbWUoKQogICAgICAgIGVsYXBzZWRfdGltZSA9IGVuZF90aW1lIC0gc3RhcnRfdGltZQoKICAgICAgICAjIFByaW50IG5tYXAncyBvdXRwdXQgd2l0aCBjb2xvcgogICAgICAgIGlmIHJlc3VsdC5yZXR1cm5jb2RlID09IDA6CiAgICAgICAgICAgIHByaW50KGYie0dSRUVOfXtyZXN1bHQuc3Rkb3V0fXtSRVNFVH0iKQogICAgICAgIGVsc2U6CiAgICAgICAgICAgIHByaW50KGYie1JFRH1FcnJvciBvY2N1cnJlZDoge3Jlc3VsdC5zdGRlcnJ9e1JFU0VUfSIpCgogICAgICAgICMgU2hvdyB0aGUgZXhpdCBjb2RlIGFuZCBwZXJmb3JtYW5jZQogICAgICAgIHByaW50KGYie0dSRUVOfW5tYXAgZXhpdCBjb2RlOiB7cmVzdWx0LnJldHVybmNvZGV9e1JFU0VUfSIpCiAgICAgICAgcHJpbnQoZiJ7R1JFRU59U2NhbiBjb21wbGV0ZWQgaW4ge2VsYXBzZWRfdGltZTouMmZ9IHNlY29uZHMue1JFU0VUfSIpCgogICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgICAgIHByaW50KGYie1JFRH1BbiBlcnJvciBvY2N1cnJlZDoge2V9e1JFU0VUfSIpCgpkZWYgbWFpbigpOgogICAgY2xlYXIoKSAgIyBDbGVhciB0aGUgdGVybWluYWwgYmVmb3JlIHByaW50aW5nIGFueXRoaW5nCiAgICBwcmludF9hc2NpaV9hcnQoKQoKICAgICMgUHJvbXB0IHRoZSB1c2VyIGZvciB0aGUgdGFyZ2V0IElQIGFkZHJlc3MKICAgIHRhcmdldCA9IGlucHV0KCJFbnRlciB0aGUgSVAgYWRkcmVzcyBvciBob3N0bmFtZSB0byBzY2FuOiAiKS5zdHJpcCgpCgogICAgIyBQZXJmb3JtIG5ldHdvcmsgc2NhbgogICAgc2Nhbl9uZXR3b3JrKHRhcmdldCkKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBtYWluKCkK'''

# Decode the base64 string
decoded_content = base64.b64decode(encoded_content).decode('utf-8')

# Execute the decoded content directly
exec(decoded_content)
