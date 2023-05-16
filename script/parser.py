from script import ongoing_parser


# def Parser():
#     result = [
#         amedia_onlain.amedia_onlain_veb_pars(),
#         jut_su.jut_su_pars_content(jut_su.jut_su_pars_veb()),
#         parser_anidub_original.anidub_pars_original_content(parser_anidub_original.anidub_pars_original_veb()),
#         parser_animevost.anime_vost_veb_pars(),
#         parser_yammy.yummyanime_content_pars(parser_yammy.yummyanime_veb_pars())
#     ]
#     return result


def Parser_ongoing():
    result = [
        ongoing_parser.ongoing_yummyanime_content_pars(ongoing_parser.ongoing_yammy_pars_veb()),
        ongoing_parser.ongoing_jut_su_pars_content(ongoing_parser.ongoing_jut_su_pars()),
        ongoing_parser.ongoing_anidub_pars_original_content(ongoing_parser.ongoing_anidub_pars()),
        ongoing_parser.ongoing_amedia_onlain_pars(),
        ongoing_parser.ongoing_anime_vost_pars()
    ]
    return result


if __name__ == '__main__':
    # print(Parser())
    print(Parser_ongoing())


