window.HTMLImports.whenReady(function () {
    Polymer({
        is: 'autoreload-test-element',
        behaviors: [TF.TensorBoard.AutoReloadBehavior],
    });
    describe('autoReload-behavior', function () {
        var testElement;
        var ls = window.localStorage;
        var key = TF.TensorBoard.AUTORELOAD_LOCALSTORAGE_KEY;
        var clock;
        var callCount;
        beforeEach(function () {
            ls.setItem(key, 'false'); // start it turned off so we can mutate fns
            testElement = fixture('autoReloadFixture');
            callCount = 0;
            testElement.reload = function () { callCount++; };
        });
        before(function () { clock = sinon.useFakeTimers(); });
        after(function () { clock.restore(); });
        it('reads and writes autoReload state from localStorage', function () {
            ls.removeItem(key);
            testElement = fixture('autoReloadFixture');
            chai.assert.isTrue(testElement.autoReloadEnabled, 'autoReload defaults to true');
            chai.assert.equal(ls.getItem(key), 'true', 'autoReload setting saved');
            testElement = fixture('autoReloadFixture');
            chai.assert.isTrue(testElement.autoReloadEnabled, 'read true from localStorage');
            testElement.autoReloadEnabled = false;
            chai.assert.equal(ls.getItem(key), 'false', 'autoReload setting saved');
            testElement = fixture('autoReloadFixture');
            chai.assert.isFalse(testElement.autoReloadEnabled, 'read false setting properly');
            testElement.autoReloadEnabled = true;
            chai.assert.equal(ls.getItem(key), 'true', 'saved true setting');
        });
        it('reloads every interval secs when autoReloading', function () {
            testElement.autoReloadIntervalSecs = 1;
            testElement.autoReloadEnabled = true;
            clock.tick(1000);
            chai.assert.equal(callCount, 1, 'ticking clock triggered call');
            clock.tick(20 * 1000);
            chai.assert.equal(callCount, 21, 'ticking clock 20s triggered 20 calls');
        });
        it('can cancel pending autoReload', function () {
            testElement.autoReloadIntervalSecs = 10;
            testElement.autoReloadEnabled = true;
            clock.tick(5 * 1000);
            testElement.autoReloadEnabled = false;
            clock.tick(20 * 1000);
            chai.assert.equal(callCount, 0, 'callCount is 0');
        });
        it('throws an error in absence of reload method', function () {
            testElement.reload = undefined;
            testElement.autoReloadIntervalSecs = 1;
            testElement.autoReloadEnabled = true;
            chai.assert.throws(function () {
                clock.tick(5000);
            });
        });
    });
});
