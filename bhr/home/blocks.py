from base.blocks import BaseStreamBlock, QuoteBlock, CarouselBlock



class BlogStreamBlock(BaseStreamBlock):
    QuoteBlock = QuoteBlock()
    CarouselBlock = CarouselBlock()