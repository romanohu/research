<%*
// 作成されたファイル名をリンクとして渡す
const fileName = tp.file.title;
const quickAddApi = app.plugins.plugins.quickadd.api;

if (quickAddApi) {
    // QuickAddのアクション（'自動リンク追加'）に、ファイル名を引数として渡す
    await quickAddApi.executeChoice('freememo', {VALUE: fileName});
}
%>