from flask import Flask, render_template, request, jsonify
import datetime
import script.search_db
import script.upgrade_db


global_html_voice = 'voice.html'
global_html_series = 'series.html'

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/series', methods=['GET', 'POST'])
def series():
    if request.method == 'GET':
        if request.args:
            anime_title = request.args.get('inputTextTitle')
            anime_series = request.args.get('inputTextSeries')
            if len(anime_series) == 0:
                anime_series = 0
            if len(anime_title) == 0:
                return ["Введите название!"]
            try:
                result = script.search_db.search_series(anime_title, int(anime_series))
                if len(result) > 0:
                    return result
                else:
                    return ["Данное аниме или серия не найдена!"]
            except:
                return ["Произошла ошибка повторите действие!"]
        else:
            return render_template(global_html_series)
    elif request.method == 'POST':
        data = request.get_json()
        anime_title = data.get('inputTextTitle')
        anime_series = data.get('inputTextSeries')
        if anime_series is None or len(anime_series) == 0:
            anime_series = 0
        if len(anime_title) == 0:
            result = ['Введите название']
            response_data = {'data': result}
            return jsonify(response_data)
        try:
            result = script.search_db.search_series(anime_title, int(anime_series))
            if len(result) > 0:
                response_data = {'data': result}
                return jsonify(response_data)
            else:
                result = ["Данное аниме или серия не найдена!"]
                response_data = {'data': result}
                return jsonify(response_data)
        except:
            result = ["Произошла ошибка повторите действие!"]
            response_data = {'data': result}
            return jsonify(response_data)


@app.route('/voice', methods=['GET', 'POST'])
def voice():
    if request.method == 'GET':
        if request.args:
            anime_title = request.args.get('inputTextTitle')
            anime_voice = request.args.get('inputTextVoice')
            if len(anime_title) == 0:
                return ["Введите название!"]
            if anime_voice == 'Voice':
                try:
                    result = script.search_db.search_none_voice(anime_title)
                    if len(result) > 0:
                        return result
                    else:
                        return ["Данное аниме не найдена!"]
                except:
                    return ["Произошла ошибка повторите действие!"]
            else:
                try:
                    result = script.search_db.search_voice(anime_title, anime_voice)
                    if len(result) > 0:
                        return result
                    else:
                        return ["Данное аниме или аниме с данной озвучкой не найдена!"]
                except:
                    return ["Произошла ошибка повторите действие!"]
        else:
            return render_template(global_html_voice)
    elif request.method == 'POST':
        data = request.get_json()
        anime_title = data.get('inputTextTitle')
        anime_voice = data.get('inputTextVoice')
        if len(anime_title) == 0:
            result = ["Введите название!"]
            response_data = {'data': result}
            return jsonify(response_data)
        if anime_voice == 'Voice':
            try:
                result = script.search_db.search_none_voice(anime_title)
                if len(result) > 0:
                    response_data = {'data': result}
                    return jsonify(response_data)
                else:
                    result = ["Данное аниме не найдена!"]
                    response_data = {'data': result}
                    return jsonify(response_data)
            except:
                result = ["Произошла ошибка повторите действие!"]
                response_data = {'data': result}
                return jsonify(response_data)
        else:
            try:
                result = script.search_db.search_voice(anime_title, anime_voice)
                if len(result) > 0:
                    response_data = {'data': result}
                    return jsonify(response_data)
                else:
                    result = ["Данное аниме или аниме с данной озвучкой не найдена!"]
                    response_data = {'data': result}
                    return jsonify(response_data)
            except:
                result = ["Произошла ошибка повторите действие!"]
                response_data = {'data': result}
                return jsonify(response_data)


@app.route('/admin/<string:password>', methods=['GET', 'POST'])
def admin(password):
    if password == 'Anim2023Web':
        if request.method == 'GET':
            if request.args:
                bool_ = request.args.get('Bool')
                if bool_ == 'ONGOING':
                    try:
                        time_start = datetime.datetime.now()
                        result = script.upgrade_db.ongoing_update()
                        time_finish = datetime.datetime.now()
                        time_ = str((time_finish - time_start).total_seconds())
                        return [time_, result]
                    except:
                        return 'Error'
                else:
                    anime_websait = request.args.get('inputTextSait')
                    anime_title = request.args.get('inputTextTitle')
                    anime_series = request.args.get('inputTextSeries')
                    return script.upgrade_db.spot_update(anime_websait, anime_title, int(anime_series))
            else:
                return render_template('admin.html')
    else:
        return render_template('update.html')


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    return render_template('contacts.html')


@app.route('/right_holders', methods=['GET', 'POST'])
def right_holders():
    return render_template('right_holders.html')


if __name__ == '__main__':
    app.run()

