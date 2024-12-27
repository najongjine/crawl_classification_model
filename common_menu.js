menu_sets = []
//메뉴 생성기 시작 S==============================
class Menu{
    constructor(mtitle){
        this.mtitle=mtitle;
    }
    mtitle;url;tips;
}
menu0 = new Menu("심심풀이 Racing Game")
menu0.url = "https://dmsgur.github.io/classification_model/race.html"
menu0.tips = "아주 기본적이고 간단한 심심풀이 땅콩 레이싱 고고~"
menu1 = new Menu("CNN AND Crawling");
menu1.url="https://dmsgur.github.io/classification_model/"
menu1.tips="네이버,구글 이미지 크롤링 및 컨볼루션 적용한 모델";
menu2 = new Menu("RNN AND LSTM encryto money")
menu2.url = "https://dmsgur.github.io/RNN_Encrypto/"
menu2.tips = "가상화폐 분석을 이용한 미래 가격 측정"
menu_sets.push(menu0)
menu_sets.push(menu1)
menu_sets.push(menu2)
