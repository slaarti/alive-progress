# pylint: disable=missing-module-docstring, possibly-unused-variable
# pylint: disable=too-many-locals
import sys
from collections import OrderedDict

from ..animations.bars import bar_factory
from ..animations.spinners import bouncing_spinner_factory, \
        sequential_spinner_factory, alongside_spinner_factory, \
        delayed_spinner_factory, frame_spinner_factory, scrolling_spinner_factory


def _wrap_ordered(context, desired):
    result = {k: v for k, v in context.items() if not k.startswith('_')}
    desired = desired.split()
    assert set(result) == set(desired), \
        'missing={}\nextra={}'.format(str(set(result) - set(desired)),
                                      str(set(desired) - set(result)))
    if sys.version_info >= (3, 7):  # python 3.7+ have dict ordering.
        return result
    return OrderedDict((x, result[x]) for x in desired)


def __create_spinners():
    classic = frame_spinner_factory(r'-\|/')
    stars = scrolling_spinner_factory('*', 4, 1, hide=False)
    twirl = frame_spinner_factory('←↖↑↗→↘↓↙')
    twirls = delayed_spinner_factory(twirl, 3)
    horizontal = frame_spinner_factory('▏▎▍▌▋▊▉█▉▊▋▌▍▎▏')
    vertical = frame_spinner_factory('▁▂▃▄▅▆▇█▇▆▅▄▃▂')
    waves = delayed_spinner_factory(vertical, 3, 2)
    waves2 = delayed_spinner_factory(vertical, 3, 5)
    waves3 = delayed_spinner_factory(vertical, 3, 7)
    dots = frame_spinner_factory('⠁⠈⠐⠠⢀⡀⠄⠂')
    dots2 = frame_spinner_factory('⣾⣷⣯⣟⡿⢿⣻⣽')
    dots_waves = delayed_spinner_factory(dots, 5)
    dots_waves2 = delayed_spinner_factory(dots, 5, 2)
    ball = scrolling_spinner_factory('●', 3, 0, background='∙')
    balls = scrolling_spinner_factory('●', 3, 1, background='∙')
    ball_belt = bouncing_spinner_factory('●', 8, 0, background='< >', hide=False)
    balls_belt = bouncing_spinner_factory('●', 8, 1, background=r'/~\_', hide=False)
    wiggle = bouncing_spinner_factory('.', 3, 3)
    wiggle2 = bouncing_spinner_factory('=', 4, 3)
    triangles = bouncing_spinner_factory(('▶', '◀'), 6, 2, hide=False)
    brackets = bouncing_spinner_factory(('>', '<'), 8, 3, hide=False)
    balloons = bouncing_spinner_factory(('∙●⦿', '○'), 10, 5, hide=False)

    notes = bouncing_spinner_factory(('♩♪', '♫♬'), 10, 4)
    notes2 = bouncing_spinner_factory(('♩♪', '♫♬'), 10, 2, hide=False)
    notes3 = delayed_spinner_factory(scrolling_spinner_factory('♩♪♫♬'), 3)

    arrow = scrolling_spinner_factory('>>----->', 15)
    arrows = bouncing_spinner_factory(('→', '←'), 6, 3)
    arrows2 = scrolling_spinner_factory('→➜➞➣➤➩➪➮', 5, 2, hide=False)
    _arrows_left = scrolling_spinner_factory('.˱·˂°❮', 6, 3, right=False)
    _arrows_right = scrolling_spinner_factory('.˲·˃°❯', 6, 3, right=True)
    arrows_in = alongside_spinner_factory(_arrows_right, _arrows_left)
    arrows_out = alongside_spinner_factory(_arrows_left, _arrows_right)

    _core = frame_spinner_factory('∙○⦿●')
    radioactive = alongside_spinner_factory(_arrows_left, _core, _arrows_right)

    boat = bouncing_spinner_factory((r'*|___/', r'\___|*'), 12, background='_.--.',
                                    hide=False, overlay=True)
    fish = scrolling_spinner_factory("><((('>", 15, hide=False)
    fish2 = bouncing_spinner_factory(("><('>", "<')><"), 12, hide=False)
    _fish_trail = scrolling_spinner_factory('¸.·´¯`·.·´¯`·.¸¸.·´¯`·.><(((º>', 15)
    _small_fishes = bouncing_spinner_factory(('><>     ><>', '<><  <><    <><'), 15)
    fishes = sequential_spinner_factory(_small_fishes, _fish_trail)
    crab = bouncing_spinner_factory((r'Y (••) Y', r'Y (  ) Y'), 15, background='.,.,,..,.,',
                                    hide=False, overlay=True)  # hey it's Ferris #rustacean!

    _look = bouncing_spinner_factory(('Look!', "It's moving!"))
    _alive = bouncing_spinner_factory(("It's alive!", "IT'S ALIVE!!"))
    frank = sequential_spinner_factory(_look, _alive)

    wait = scrolling_spinner_factory('please wait...', right=False)
    wait2 = bouncing_spinner_factory(('please', 'wait'), 15, hide=False)
    wait3 = bouncing_spinner_factory(('processing',
                                      'well, this is taking longer than anticipated, hold on'), 15)
    pulse = frame_spinner_factory(
        r'•–––––––––––––',
        r'–•––––––––––––',
        r'––•–––––––––––',
        r'–––•––––––––––',
        r'––––•–––––––––',
        r'–––––√––––––––',
        r'–––––√\–––––––',
        r'–––––√\/––––––',
        r'–––––√\/•–––––',
        r'–––––√\/–•––––',
        r'––––––\/––•–––',
        r'–––––––/–––•––',
        r'––––––––––––•–',
        r'–––––––––––––•',
    )

    return _wrap_ordered(
        locals(),
        'classic stars twirl twirls horizontal vertical waves waves2 waves3 dots dots2'
        ' dots_waves dots_waves2 ball balls ball_belt balls_belt wiggle wiggle2 arrow arrows'
        ' arrows2 arrows_in arrows_out triangles brackets balloons notes notes2 notes3 radioactive'
        ' boat fish fish2 fishes crab frank wait wait2 wait3 pulse'
    )


SPINNERS = __create_spinners()


def __create_bars():
    smooth = bar_factory('▏▎▍▌▋▊▉█')
    classic = bar_factory('=', tip='>', borders='[]', errors='!x')
    classic2 = bar_factory('#', background='.', borders='[]', errors='!x')
    brackets = bar_factory('>')
    blocks = bar_factory('▏▎▍▌▋▊▉')
    bubbles = bar_factory('∙○⦿●', borders='<>')
    hollow = bar_factory('❒', tip='▷', borders='<>')
    solid = bar_factory('■', tip='►', borders='<>')
    circles = bar_factory('●', background='○', borders='<>')
    squares = bar_factory('■', background='❒', borders='<>')
    checks = bar_factory('✓')
    filling = bar_factory('▁▂▃▄▅▆▇█')
    notes = bar_factory('♩♪♫', borders='𝄞𝄢', errors='♭♯')
    ruler = bar_factory('', tip='┃', background='∙∙∙∙•')
    ruler2 = bar_factory('', tip='┃', background='∙∙∙∙+')
    underwater = bar_factory('', tip='>=≗)o', background='_)_)._∙__⠈__)○____∙○___)__⠈(_(__')

    return _wrap_ordered(
        locals(),
        'smooth classic classic2 brackets blocks bubbles hollow solid circles squares checks'
        ' filling notes ruler ruler2 underwater'
    )


BARS = __create_bars()


def __create_themes():
    smooth = dict(bar='smooth', spinner='waves', unknown='triangles')
    classic = dict(bar='classic', spinner='classic', unknown='brackets')
    scuba = dict(bar='underwater', spinner='fish2', unknown='fishes')  # I love scuba-diving.
    musical = dict(bar='notes', spinner='notes2', unknown='notes3')

    return _wrap_ordered(locals(), 'smooth classic scuba musical')


THEMES = __create_themes()
