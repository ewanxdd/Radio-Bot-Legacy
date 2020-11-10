def is_super(ctx):
    if ctx.message.author.id == 210885581264125952:
        return True

def is_maintainer(ctx):
    if ctx.message.author.id == 210885581264125952 or ctx.message.author.id == 249919528421556224 or ctx.message.author.id == 190935064887033856:
        return True
