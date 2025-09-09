import base64


class DecodeList:

    def __init__(self):
        self.hostile = "R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT"
        self.less_hostile = "RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=="


    def decode_hostile_list(self):
        hostile_list = base64.b64decode(self.hostile).decode("utf-8").split(',')
        return hostile_list

    def decode_less_hostile_list(self):
        hostile_list = base64.b64decode(self.less_hostile).decode("utf-8").split(',')
        return hostile_list

print(DecodeList().decode_less_hostile_list())