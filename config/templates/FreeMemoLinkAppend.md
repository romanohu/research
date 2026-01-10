<%*
// QuickAddで作成した「目次追記」などのアクション名を指定します
const actionName = '目次追記'; 

const quickAddApi = app.plugins.plugins.quickadd.api;
if (quickAddApi) {
    await quickAddApi.executeChoice(actionName);
} else {
    new Notice("QuickAddプラグインが見つかりません");
}
%>