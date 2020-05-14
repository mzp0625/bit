from marshmallow import Schema, fields


class TagFormSchema(Schema):
    name = fields.Str(required=True)
    summary = fields.Str(required=True)
    submission_guidelines = fields.Str(required=True)
    about = fields.Str(required=True)

    class Meta:
        # Fields to show when sending data
        fields = ("name", "summary", "submission_guidelines", "about")
        ordered = True


class TagSchema(Schema):
    id = fields.Int(required=True)

    class Meta:
        # Fields to show when sending data
        fields = ("id")
        ordered = True


tag_form_schema = TagFormSchema()
tag_schema = TagSchema()
tags_schema = TagSchema(many=True)