menu_sets = []
//메뉴 생성기 시작 S==============================
class Menu{
    constructor(mtitle){
        this.mtitle=mtitle;
    }
    mtitle;url;tips;
}
menu1 = new Menu("CNN AND Crawling");
menu1.url="https://dmsgur.github.io/classification_model/"
menu1.tips="네이버,구글 이미지 크롤링 및 컨볼루션 적용한 모델";
menu2 = new Menu("test menu")
menu2.url = "127.0.0.1"
menu2.tips = "테스트용 메뉴"
menu_sets.push(menu1)
menu_sets.push(menu2)