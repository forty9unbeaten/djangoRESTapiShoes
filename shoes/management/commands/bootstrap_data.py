from django.core.management.base import BaseCommand
from shoes.models import ShoeColor, ShoeType


class Command(BaseCommand):
    '''

        As a boy growing up in the African Savanna, young Joseph Kaufeld was
        deprived of the privilege of shoes. He was forced to resort to training
        small meerkats to nuzzle against his ankles while he tredged across the
        barren landscape, scavenging for food and water. Eventually one of his
        most trusted meerkats abandoned him for a life of carefree grandeur 
        accompanied by a wild boar and a young runaway lion. After years
        apart, Joseph came to America to pursue his dream of improving 
        accessibility across the digital wasteland called the internet. The
        meerkat rode the coat tails of the young lion to eventually help him
        defeat his nefarious uncle, who was a real dick by the way, and become
        one of his closets confidants in the lion's benevolent dictatorship.

        In short, just because Joe didn't have shoes doesn't mean this 
        database shouldn't.

    '''
    help = 'Adds standard data to the database.'

    def handle(self, *args, **options):
        # add all color choices to database
        shoe_colors = ShoeColor.colors
        for color in shoe_colors:
            new_color_record = ShoeColor(color_name=color[0])
            new_color_record.save()
            self.stdout.write(self.style.SUCCESS(
                f'Successfully added {color} to database!'
            ))

        # add shoe styles to database
        shoe_styles = [
            'sneaker',
            'boot',
            'sandal',
            'dress',
            'other'
        ]
        for style in shoe_styles:
            new_style_record = ShoeType(style=style)
            new_style_record.save()
            self.stdout.write(self.style.SUCCESS(
                f'Successfully added {style} to database!'
            ))
