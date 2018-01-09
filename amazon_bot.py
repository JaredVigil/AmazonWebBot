import requests
import time
from bs4 import BeautifulSoup as bs
from robobrowser import RoboBrowser


session = requests.session()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'
parser = "html.parser"
browser = RoboBrowser(session=session, user_agent=user_agent, parser="html.parser")



def login():
    global browser
    urlHome = "https://www.amazon.com/"
    browser.open(urlHome)
    url = "https://www.amazon.com/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=usflex&openi" \
          "d.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3" \
          "A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%" \
          "3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2F" \
          "pape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_ya" \
          "_signin&switch_account="
    browser.open(url)
    form = browser.get_form()
    form['email'] = 'youEmail@gmail.com'
    form['password'] = 'youPassword'
    form['rememberMe'] = 'true'
    browser.session.headers.update({
        'Referer': url,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5'
    })
    browser.submit_form(form)
    browser.open(urlHome)
    print("LOGIN")



def logout():
    global browser
    session = browser.session
    url0 = "https://www.amazon.com/gp/flex/sign-out.html/ref=nav_youraccount_signout?ie=UTF8&action=sign-out&path=%2Fgp%2Fyourstore%2Fhome&signIn=1&useRedirectOnSuccess=1"
    res0 = session.get(url0)
    print("LOGOUT")



def checkStock():
    global browser
    session = browser.session
    available = False
    soup = None
    url0 = "https://www.amazon.com/Fingerlings-Glitter-Monkey-Amazon-Exclusive/dp/B06XSZVJ4K"
    url1 = "https://www.amazon.com/dp/B0046XG48O/ref=sspa_dk_detail_2?psc=1&pd_rd_i=B0046XG48O&pd_rd_wg=lX1zN&pd_rd_r=0S0Z8MF2HKSCZ2RKPK7J&pd_rd_w=p1U3D&smid=A2RQ38FFUL7LO9"
    url2 = "https://www.amazon.com/gp/product/B01H2JPTDO/ref=oh_aui_detailpage_o01_?ie=UTF8&psc=1"
    url3 = "https://www.amazon.com/dp/B01N2HNDYU/ref=strm_fun_197_nad_1_3"
    while not available:
        res0 = session.get(url0)
        soup = bs(res0.text,"html.parser")
        snap = soup.find("a",{"title":"Email Me"})
        if snap is None and res0.status_code == 200:
            available = True
        else:
            time.sleep(60)

    sessionId = soup.find("input", {"id": "session-id"})
    asin = soup.find("input", {"id": "ASIN"})
    offerListingID = soup.find("input", {"id": "offerListingID"})
    isMerchantExclusiveId= soup.find("input", {"id": "isMerchantExclusive"})
    merchantID = soup.find("input",{"id":"merchantID"})
    isAddon = soup.find("input",{"id":"isAddon"})
    nodeID = soup.find("input",{"id":"nodeID"})
    sellingCustomerID = soup.find("input", {"id": "sellingCustomerID"})
    qid = soup.find("input", {"id": "qid"})
    sr = soup.find("input", {"id": "sr"})
    storeID = soup.find("input", {"id": "storeID"})
    tagActionCode = soup.find("input", {"id": "tagActionCode"})
    viewID = soup.find("input", {"id": "viewID"})
    sourceCustomerOrgListID = soup.find("input", {"id": "sourceCustomerOrgListID"})
    sourceCustomerOrgListItemID = soup.find("input", {"id": "sourceCustomerOrgListItemID"})
    wlPopCommand = soup.find("input", {"id": "wlPopCommand"})

    sessionIdValue = sessionId["value"]
    asinValue = asin["value"]
    offerListingIDValue = offerListingID["value"]
    isMerchantExclusiveIdValue = isMerchantExclusiveId["value"]
    merchantIDValue = merchantID["value"]
    isAddonValue = isAddon["value"]
    nodeIDValue = nodeID["value"]
    sellingCustomerIDValue = sellingCustomerID["value"]
    qidValue = qid["value"]
    srValue = sr["value"]
    storeIDValue = storeID["value"]
    tagActionCodeValue = tagActionCode["value"]
    viewIDValue = viewID["value"]
    sourceCustomerOrgListIDValue = sourceCustomerOrgListID["value"]
    sourceCustomerOrgListItemIDValue = sourceCustomerOrgListItemID["value"]
    wlPopCommandValue = ""
    if wlPopCommand is not None:
        wlPopCommandValue = wlPopCommand["value"]

    data = {
        "session-id": sessionIdValue,
        "ASIN": asinValue,
        "offerListingID":offerListingIDValue,
        "isMerchantExclusive": isMerchantExclusiveIdValue,
        "merchantID": merchantIDValue,
        "isAddon": isAddonValue,
        "nodeID": nodeIDValue,
        "sellingCustomerID": sellingCustomerIDValue,
        "qid": qidValue,
        "sr": srValue,
        "storeID": storeIDValue,
        "tagActionCode": tagActionCodeValue,
        "viewID": viewIDValue,
        "rsid": sessionIdValue,
        "sourceCustomerOrgListID": sourceCustomerOrgListIDValue,
        "sourceCustomerOrgListItemID": sourceCustomerOrgListItemIDValue,
        "wlPopCommand": wlPopCommandValue,
        "quantity": "1",
        "submit.add-to-cart": "Add to Cart",
        "dropdown-selection": "add-new"
    }
    print("IN STOCK")
    return data


def putInCart():
    global browser
    session = browser.session
    data = checkStock()
    url0 = "https://www.amazon.com/gp/product/handle-buy-box/ref=dp_start-bbf_1_glance"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    res0 = session.post(url0,headers=headers,data=data)
    url1 = "https://www.amazon.com/gp/cart/view.html/ref=lh_cart"
    res1 = session.get(url1,headers=headers)

    print("PUT IT IN CART")

def checkOut():
    global browser
    session = browser.session
    url0 = "https://www.amazon.com/gp/cart/desktop/go-to-checkout.html/ref=ox_sc_proceed?isToBeGiftWrappedBe" \
           "fore=&proceedToCheckout=Proceed+to+checkout&cartInitiateId=1513825491221"
    res0 = session.get(url0)
    print("CHECKOUT")

def purchaseItem():
    global browser
    url0 = "https://www.amazon.com/gp/buy/spc/handlers/display.html?hasWorkingJavascript=1"
    session = browser.session
    res0 = session.get(url0)
    soup = bs(res0.text,"html.parser")
    fasttrackExpiration = soup.find("input",{"name":"fasttrackExpiration"})
    countdownThreshold = soup.find("input",{"name":"countdownThreshold"})
    showSimplifiedCountdown = soup.find("input",{"name":"showSimplifiedCountdown"})
    countdownId = soup.find("input",{"name":"countdownId"})
    quantity_A06038462WL80R1QDG993 = soup.find("input",{"id":"quantity.A06038462WL80R1QDG993:"})
    gift_message_text = soup.find("input",{"name":"gift-message-text"})
    dupOrderCheckArgs = soup.find("input",{"name":"dupOrderCheckArgs"})
    order0 = soup.find("input",{"name":"order0"})
    shippingofferingid0_0 = soup.find("input",{"name":"shippingofferingid0.0"})
    guaranteetype0_0 = soup.find("input",{"name":"guaranteetype0.0"})
    issss0_0 = soup.find("input",{"name":"issss0.0"})
    forceshipsplitpreference0_0 = soup.find("input",{"name":"forceshipsplitpreference0.0"})
    shippingofferingid0_1 = soup.find("input",{"name":"shippingofferingid0.1"})
    guaranteetype0_1 = soup.find("input",{"name":"guaranteetype0.1"})
    issss0_1 = soup.find("input",{"name":"issss0.1"})
    forceshipsplitpreference0_1 = soup.find("input",{"name":"forceshipsplitpreference0.1"})
    previousshippingofferingid0 = soup.find("input",{"name":"previousshippingofferingid0"})
    previousguaranteetype0 = soup.find("input",{"name":"previousguaranteetype0"})
    previousissss0 = soup.find("input",{"name":"previousissss0"})
    previousshippriority0 = soup.find("input",{"name":"previousshippriority0"})
    lineitemids0 = soup.find("input",{"name":"lineitemids0"})
    currentshippingspeed = soup.find("input",{"name":"currentshippingspeed"})
    previousShippingSpeed0 = soup.find("input",{"name":"previousShippingSpeed0"})
    currentshipsplitpreference = soup.find("input",{"name":"currentshipsplitpreference"})
    shippriority_0_shipWhenever = soup.find("input",{"name":"shippriority.0.shipWhenever"})
    groupcount = soup.find("input",{"name":"groupcount"})
    fixgroupcount = soup.find("input",{"name":"fixgroupcount"})
    shiptrialprefix = soup.find("input",{"name":"shiptrialprefix"})
    fromAnywhere = soup.find("input",{"name":"fromAnywhere"})
    redirectOnSuccess = soup.find("input",{"name":"redirectOnSuccess"})
    purchaseTotal = soup.find("input",{"name":"purchaseTotal"})
    purchaseTotalCurrency = soup.find("input",{"name":"purchaseTotalCurrency"})
    purchaseID = soup.find("input",{"name":"purchaseID"})
    purchaseCustomerId = soup.find("input",{"name":"purchaseCustomerId"})
    useCtb = soup.find("input",{"name":"useCtb"})
    scopeId = soup.find("input",{"name":"scopeId"})
    isQuantityInvariant = soup.find("input",{"name":"isQuantityInvariant"})
    promiseTime_0 = soup.find("input",{"name":"promiseTime-0"})
    promiseAsin_0 = soup.find("input",{"name":"promiseAsin-0"})
    isfirsttimecustomer = soup.find("input",{"name":"isfirsttimecustomer"})
    isTFXEligible = soup.find("input",{"name":"isTFXEligible"})
    isFxEnabled = soup.find("input",{"name":"isFxEnabled"})
    isFXTncShown = soup.find("input",{"name":"isFXTncShown"})

    fasttrackExpirationValue = fasttrackExpiration["value"]
    countdownThresholdValue = countdownThreshold["value"]
    showSimplifiedCountdownValue = showSimplifiedCountdown["value"]
    countdownIdValue = countdownId["value"]
    quantity_A06038462WL80R1QDG993_value = "1"
    gift_message_text_value = ""
    dupOrderCheckArgsValue = dupOrderCheckArgs["value"]
    order0Value = order0["value"]
    shippingofferingid0_0Value = shippingofferingid0_0["value"]
    guaranteetype0_0Value = guaranteetype0_0["value"]
    issss0_0Value = issss0_0["value"]
    forceshipsplitpreference0_0Value = forceshipsplitpreference0_0.text
    shippingofferingid0_1Value = shippingofferingid0_1["value"]
    guaranteetype0_1Value = guaranteetype0_1["value"]
    issss0_1Value = issss0_1["value"]
    forceshipsplitpreference0_1Value = forceshipsplitpreference0_1.text
    previousshippingofferingid0Value = previousshippingofferingid0["value"]
    previousguaranteetype0Value = previousguaranteetype0["value"]
    previousissss0Value = previousissss0["value"]
    previousshippriority0Value = previousshippriority0["value"]
    lineitemids0Value = lineitemids0["value"]
    currentshippingspeedValue = currentshippingspeed["value"]
    previousShippingSpeed0Value = previousShippingSpeed0["value"]
    currentshipsplitpreferenceValue = currentshipsplitpreference["value"]
    shippriority_0_shipWheneverValue = shippriority_0_shipWhenever["value"]
    groupcountValue = groupcount["value"]
    fixgroupcountValue = fixgroupcount["value"]
    shiptrialprefixValue = shiptrialprefix["value"]
    fromAnywhereValue = fromAnywhere["value"]
    redirectOnSuccessValue = redirectOnSuccess["value"]
    purchaseTotalValue = purchaseTotal["value"]
    purchaseTotalCurrencyValue = purchaseTotalCurrency["value"]
    purchaseIDValue = purchaseID["value"]
    purchaseCustomerIdValue = purchaseCustomerId["value"]
    useCtbValue = useCtb["value"]
    scopeIdValue = scopeId["value"]
    isQuantityInvariantValue = isQuantityInvariant.text
    promiseTime_0Value = promiseTime_0["value"]
    promiseAsin_0Value = promiseAsin_0["value"]
    hasWorkingJavascriptValue = "1"
    placeYourOrder1Value = "1",
    isfirsttimecustomerValue = isfirsttimecustomer["value"]
    isTFXEligibleValue = isTFXEligible.text
    isFxEnabledValue = isFxEnabled.text
    isFXTncShownValue = isFXTncShown.text

    data = {
        "fasttrackExpiration": fasttrackExpirationValue,
        "countdownThreshold": countdownThresholdValue,
        "showSimplifiedCountdown": showSimplifiedCountdownValue,
        "countdownId": countdownIdValue,
        "quantity.A06038462WL80R1QDG993:":quantity_A06038462WL80R1QDG993_value,
        "gift-message-text": gift_message_text_value,
        "dupOrderCheckArgs": dupOrderCheckArgsValue,
        "order0": order0Value,
        "shippingofferingid0.0": shippingofferingid0_0Value,
        "guaranteetype0.0": guaranteetype0_0Value,
        "issss0.0": issss0_0Value,
        "forceshipsplitpreference0.0":forceshipsplitpreference0_0Value,
        "shippingofferingid0.1": shippingofferingid0_1Value,
        "guaranteetype0.1": guaranteetype0_1Value,
        "issss0.1": issss0_1Value,
        "forceshipsplitpreference0.1":forceshipsplitpreference0_1Value,
        "previousshippingofferingid0":previousshippingofferingid0Value,
        "previousguaranteetype0": previousguaranteetype0Value,
        "previousissss0": previousissss0Value,
        "previousshippriority0": previousshippriority0Value,
        "lineitemids0": lineitemids0Value,
        "currentshippingspeed": currentshippingspeedValue,
        "previousShippingSpeed0": previousShippingSpeed0Value,
        "currentshipsplitpreference": currentshipsplitpreferenceValue,
        "shippriority.0.shipWhenever": shippriority_0_shipWheneverValue,
        "groupcount":groupcountValue,
        "fixgroupcount": fixgroupcountValue,
        "shiptrialprefix": shiptrialprefixValue,
        "fromAnywhere": fromAnywhereValue,
        "redirectOnSuccess": redirectOnSuccessValue,
        "purchaseTotal": purchaseTotalValue,
        "purchaseTotalCurrency": purchaseTotalCurrencyValue,
        "purchaseID": purchaseIDValue,
        "purchaseCustomerId": purchaseCustomerIdValue,
        "useCtb": useCtbValue,
        "scopeId": scopeIdValue,
        "isQuantityInvariant":isQuantityInvariantValue,
        "promiseTime-0":promiseTime_0Value,
        "promiseAsin-0": promiseAsin_0Value,
        "hasWorkingJavascript": hasWorkingJavascriptValue,
        "placeYourOrder1": placeYourOrder1Value,
        "isfirsttimecustomer": isfirsttimecustomerValue,
        "isTFXEligible": isTFXEligibleValue,
        "isFxEnabled":isFxEnabledValue,
        "isFXTncShown":isFXTncShownValue,
    }
    url1 = "https://www.amazon.com/gp/buy/spc/handlers/static-submit-decoupled.html/ref=ox_spc_place_order?ie=UTF8&hasWorkingJavascript="
    res1 = session.post(url1,data=data)
    print("PURCHASE")




login()
putInCart()
checkOut()
purchaseItem()
logout()
